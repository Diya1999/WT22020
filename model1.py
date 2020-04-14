import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import itertools
from sklearn.utils import resample
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import resample
import pickle
import joblib
import io
import seaborn as sns
import plotly.graph_objects as go
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix,auc,roc_auc_score,precision_score,recall_score

train_data =pd.read_csv("train_2v.csv")
test_data =pd.read_csv("test_2v.csv")
train_data["bmi"]=train_data["bmi"].fillna(train_data["bmi"].mean())
#dropping ID column
train_data=train_data.drop(columns="id")
#label = LabelEncoder()
le_gender = LabelEncoder()
le_married = LabelEncoder()                      
le_work= LabelEncoder()    
le_residence=LabelEncoder() 
le_smoke= LabelEncoder() 
le_gender.fit(["Male","Female","Other"])
le_married.fit(["Yes","No"])
le_work.fit(["children","Private","Never_worked","Self-employed","Govt_job"])
le_residence.fit(["Urban","Rural"])
train_data['gender'] = le_gender.fit_transform(train_data['gender'])
train_data['ever_married'] = le_married .fit_transform(train_data['ever_married'])
train_data['work_type']= le_work.fit_transform(train_data['work_type'])
train_data['Residence_type']= le_residence.fit_transform(train_data['Residence_type'])
train_data_without_smoke = train_data[train_data['smoking_status'].isnull()]
train_data_with_smoke = train_data[train_data['smoking_status'].notnull()]
train_data_without_smoke.drop(columns='smoking_status',axis=1,inplace=True)
le_residence.fit_transform(train_data['Residence_type'])
train_data_with_smoke['smoking_status']= le_smoke.fit_transform(train_data_with_smoke['smoking_status'])
#resampling for data balancing 
majority=train_data_without_smoke[train_data_without_smoke.stroke==0]
minority1=train_data_without_smoke[train_data_without_smoke.stroke==1]
minority_upsampled1=resample(minority1, replace=True, n_samples=len(majority), random_state=1)
upsampled=pd.concat([majority,minority_upsampled1])
y_resampled=upsampled.stroke
X_resampled=upsampled.drop("stroke",axis=1)
#apply the model
X_train,X_test,y_train,y_test = train_test_split(X_resampled,y_resampled,test_size=0.2)
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

pred = dtree.predict(X_test)
#print(classification_report(y_test,pred))
#print (accuracy_score(y_test,pred))
#print (confusion_matrix(y_test,pred))

#save model
filename = 'decision_trees.sav'
pickle.dump(dtree, open(filename, 'wb'))

def prediction(gender1,age1,hyp1,heart1,married1,work1,residence1,glucose1,bmi1):
    #id1,gender1,age1,hyp1,heart1,married1,work1,residence1,glucose1,bmi1
    le_gender = LabelEncoder()
    le_married = LabelEncoder()                      
    le_work= LabelEncoder()    
    le_residence=LabelEncoder() 
    le_smoke= LabelEncoder() 
    le_gender.fit(["Male","Female","Other"])
    le_married.fit(["Yes","No"])
    le_work.fit(["children","Private","Never_worked","Self-employed","Govt_job"])
    le_residence.fit(["Urban","Rural"])
    dt = joblib.load('decision_trees.sav')  
    data = [[gender1,age1,hyp1,heart1,married1,work1,residence1,glucose1,bmi1]] 
    newinput = pd.DataFrame(data, columns = ['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi']) 
    newinput['gender'] = le_gender.transform(newinput['gender'])
    #newinput['ever_married'] = le_married .fit_transform(newinput['ever_married'])
    newinput['work_type']= le_work.transform(newinput['work_type'])
    newinput['Residence_type']= le_residence.transform(newinput['Residence_type'])
    #dt.predict(newinput) 
    output=dt.predict(newinput) 
    if(output[0]==1):
        return "STROKE: KINDLY TAKE NECESSARY PRECAUTIONS"
    else:
        return "NO STROKE"


def corr():
    corr = train_data.corr()
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    mask = np.zeros_like(corr, dtype=np.bool)
    #mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5})
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def confusion_matrix_rep():
    model="Decision Tree"
    class_names=train_data.stroke.unique()
    class_names=list(class_names)
    cm=confusion_matrix(y_test, pred, labels=class_names)
    #print("recall:",metrics.recall_score(y_test, y_pred,average='macro'))
    cm=confusion_matrix(y_test, pred, labels=class_names)
    #print("confusion matrix:\n\n" ,cm)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm,cmap=plt.cm.Blues)
    plt.title('Confusion matrix for '+model+" model", y=-0.5)
    fmt = 'd'
    # write the number of predictions in each bucket
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    # if background is dark, use a white number, and vice-versa
        plt.text(j, i, format(cm[i, j], fmt),
         horizontalalignment="center",
         color="white" if cm[i, j] > thresh else "black")
    fig.colorbar(cax)
    ax.set_xticklabels([''] + class_names)
    ax.set_yticklabels([''] + class_names)
    ax.tick_params(axis='x', rotation=90)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    #plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def metrics1():
    F1 = metrics.f1_score(y_test,pred)
    precision = precision_score(y_test,pred)
    recall = recall_score(y_test,pred)
    buff="Precision = "+str(precision)+"\t\n"+"Recall = "+str(recall)+"\t\n"+"F1 Score = "+str(F1)
    return(buff)