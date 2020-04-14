from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_file
from flask import make_response
import model1
from flask import request
from flask import Flask, render_template
import pandas as pd
import numpy
import not1
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, resources={r'/*/*': {'origins': '*'}})
# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#used in AddData.vue
@app.route('/getEntry/<id>', methods=['POST'])
def getEntry(id):
    post_data = request.get_json()
    idcheck=int(post_data['id'])
    train_data =pd.read_csv("train_2v.csv")
    row= -1
    for i in range(len(train_data)):
        row=-1
        a=train_data.loc[i,'id']
        a=int(a)
        if(a==idcheck):
            print("FOUND",i)
            row=i
            break
    if(row==-1):
        return jsonify({'Error':'No such ID'})
    response_object ={ 'id':a,'age':int(train_data.loc[row,'age']),'gender':train_data.loc[row,'gender'],'strokes':int(train_data.loc[row,'stroke'])}
    return jsonify(response_object)


#used inAddData.vue
@app.route('/addData', methods=['POST'])
def addData():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    #print("post",post_data)
    train_data =pd.read_csv("train_2v.csv")
    #print(post_data)
    response_object['message'] = 'Record added!'
    id=numpy.int64(post_data['id'])
    row= -1
    for i in range(len(train_data)):
        row=-1
        a=train_data.loc[i,'id']
        a=int(a)
        if(a==id):
            print("FOUND",i)
            row=i
            break
    if(row!=-1):
        return jsonify({'message':'ID already present!!'})
    gender=post_data['gender']
    age=numpy.int64(post_data['age'])
    Residence_type= post_data['Residence_type']
    hypertension=post_data['hypertension']
    if(hypertension==False):
        hypertension=numpy.int64(0)
    else:
        hypertension=numpy.int64(1)
    ever_married=post_data['ever_married']
    if(ever_married==False):
        ever_married="No"
    else:
        ever_married="Yes"
    heart_disease=post_data["heart_disease"]
    if(heart_disease==False):
        heart_disease=numpy.int64(0)
    else:
        heart_disease=numpy.int64(1)
    work_type=post_data["work_type"]
    avg_glucose_level=numpy.int64(post_data["avg_glucose_level"])
    bmi=numpy.int64(post_data["bmi"])
    smoking_status=post_data["smoking_status"]
    stroke=post_data["stroke"]
    if(stroke==False):
        stroke=numpy.int64(0)
    else:
        stroke=numpy.int64(1)
    main={'id':id , 'gender': gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease, 'ever_married': ever_married, 'work_type': work_type, 'Residence_type': Residence_type, 'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status, 'stroke': stroke}
    #print(main , "\n--------------------------------\n") 
    # a=pd.DataFrame([main])
    # print(a['id'])
    # train_data.append(a, ignore_index = True)
    train_data.loc[len(train_data.index)]=list(main.values())
    train_data.to_csv('train_2v.csv', index=False)
    #print(train_data.loc[-1, 'id'])
    return jsonify(response_object)
  #  return jsonify('pong!')

@app.route('/delEntry/<id>', methods=['DELETE'])
def delete_task(id):
    train_data =pd.read_csv("train_2v.csv")
    idcheck=int(id)
    row= -1
    for i in range(len(train_data)):
        row=-1
        a=train_data.loc[i,'id']
        a=int(a)
        if(a==idcheck):
            print("FOUND",i)
            row=i
            break
    if(row==-1):
        return jsonify({'message': "No such ID!!"})
    print(row)
    train_data=train_data[train_data.id != numpy.int64(idcheck)]
    train_data.to_csv('train_2v.csv', index=False)
    return jsonify({'message': "Deleted successfully!"})

@app.route('/predict', methods=['POST'])
def pred():
    response_object = {'status': 'success'}
    content = request.get_json()
    #print(content['gender'])
    #print(content['work_type'].strip())
    gender=content['gender']
    #gender='Female'
    age=int(content['age'])
   
    #age=10
    hypertension=content['hypertension']
    #hypertension=0
    heart=content['heart_disease']
    #heart=0
    married=content['ever_married']
    #married=1
    if(hypertension=="False"):
        hypertension=0 
    elif(hypertension=="True"):
        hypertension=1
    if(heart=="False"):
        heart=0
    elif(heart=="True"):
        heart=1
    if(married=="False"):
        married=0
    elif(married=="True"):
        married=1
    work=content['work_type'].strip()
    #work='Private'
    residence=content['Residence_type']
    #residence='Urban'
    glucose=float(content['avg_glucose_level'])
    #glucose= 12
    bmi=float(content['bmi'])
    #bmi=10
    #response_object['message'] = 'Record added!'
    bytes_obj = model1.prediction(gender,age,hypertension,heart,married,work,residence,glucose,bmi) 
    print(bytes_obj)
    #if id already exists,
    #response_object['message'] = 'ID already present!!'
    return jsonify(bytes_obj)
  #  return jsonify('pong!')

@app.route('/metrics', methods=['GET'])
def met():
    bytes_obj = model1.metrics1() 
    temp= bytes_obj
    temp= temp.splitlines()
    {'Precision':temp[0],'Recall':temp[1],'F1Score':temp[2]}
    print(temp)
    return jsonify({'Precision':temp[0],'Recall':temp[1],'F1Score':temp[2]})

@app.route('/correlation', methods=['GET'])
def corr():
    bytes_obj = model1.corr() 
    #print(send_file(bytes_obj,attachment_filename='plot.png',mimetype='image/png'))
    return send_file(bytes_obj,attachment_filename='plot.png',mimetype='image/png')
    #return bytes_obj

@app.route('/confusion', methods=['GET'])
def conf():
    bytes_obj = model1.confusion_matrix_rep() 
    return send_file(bytes_obj,
                     attachment_filename='plot1.png',
                     mimetype='image/png')

@app.route('/plots/0', methods=['GET'])
def scatterplot0():
    bytes_obj = not1.plot0() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/1', methods=['GET'])
def scatterplot1():
    bytes_obj = not1.plot1() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/2', methods=['GET'])
def scatterplot2():
    bytes_obj = not1.plot2() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/3', methods=['GET'])
def scatterplot3():
    bytes_obj = not1.plot3() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/4', methods=['GET'])
def scatterplot4():
    bytes_obj = not1.plot4() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/5', methods=['GET'])
def scatterplot5():
    bytes_obj = not1.plot5() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/6', methods=['GET'])
def scatterplot6():
    bytes_obj = not1.plot6() 
    print(bytes_obj)
    return bytes_obj

@app.route('/plots/7', methods=['GET'])
def scatterplot7():
    bytes_obj = not1.plot7() 
    print(bytes_obj)
    return bytes_obj

if __name__ == '__main__':
    app.run()
