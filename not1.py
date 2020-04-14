import plotly.express as px
import chart_studio.plotly as py
import chart_studio
import chart_studio.tools as tls
import pandas as pd
import numpy as np

df=pd.read_csv("train_2v.csv")
df['bmi'] = df['bmi'].replace(np.nan, 0)
df['smoking_status'] = df['smoking_status'].replace(np.nan, "Data Unavailable")
stroke=df[df['stroke']== 1]
nostroke=df[df['stroke']== 0]
#removing missing rows from no stroke
nostroke=nostroke[nostroke['bmi']!= 0]
nostroke=nostroke[nostroke['smoking_status']!= "Data Unavailable"]
nostroke=nostroke.head(n=25000)
usedf=pd.concat([stroke,nostroke])
#labelled stroke
df2=usedf
df2['stroke'] = df2['stroke'].replace(0, "No Stroke")
df2['stroke'] = df2['stroke'].replace(1, "Stroke")
#bmi and smoking status
strokebmi=stroke[stroke['bmi']!=0]
strokesmoke=stroke[stroke['smoking_status']!="Data Unavailable"]
strokebmismoke=strokesmoke[strokesmoke['bmi']!=0]

def intro():
    return "A stroke, or \"brain attack,\" occurs when blood circulation to the brain fails. Brain cells can die from decreased blood flow and the resulting lack of oxygen.There are two broad categories of stroke: those caused by a blockage of blood flow and those caused by bleeding into the brain. A blockage of a blood vessel in the brain or neck, called an ischemic stroke, is the most frequent cause of stroke and is responsible for about 80 percent of strokes.These blockages stem from three conditions: the formation of a clot within a blood vessel of the brain or neck, called thrombosis; the movement of a clot from another part of the body such as the heart to the brain, called embolism; or a severe narrowing of an artery in or leading to the brain, called stenosis. Bleeding into the brain or the spaces surrounding the brain causes the second type of stroke, called hemorrhagic stroke.Thus, an analysis was done on 43,200 test subjects. Various factors such as gender, age, bmi, hypertension, etc were analysed.The aim of this analysis is to find the main causes and the risks associated with strokes in humans.The following visualizations provide insights are that clear, comprehensive and acts as evidence to the conclusions that will be made at the end of the study"

def plot0():
    # Loading 
    fig0= px.scatter(strokebmi, x="bmi", y="age",color="ever_married",
           hover_name="work_type",  size_max=60,title="Plot of Body Mass Index and age with respect to marital status and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig0, filename = '1', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    iframe1=tls.get_embed(url)
    return iframe1

def plot1():
    # Loading 
    fig1= px.scatter(strokebmi, x="bmi", y="avg_glucose_level",color="gender",
           hover_name="work_type" , size_max=60,title="Plot of Body Mass Index and Average Glucose level with respect to gender and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig1, filename = '2', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    iframe1=tls.get_embed(url)
    return iframe1

def plot2():
    # Loading 
    fig2= px.scatter(strokebmismoke, x="bmi", y="age",color="smoking_status",
           hover_name="work_type",  size_max=60,title="Plot of Body Mass Index and age with respect to work status and smoking status")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig2, filename = '3', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1


def plot3():
    # Loading 
    fig3= px.scatter(strokesmoke, x="avg_glucose_level", y="age",color="smoking_status",
           hover_name="work_type",  size_max=60,title="Plot of Average Glucose Level and age with respect to smoking status and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'# your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig3, filename = '4', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot4():
    # Loading 
    fig4= px.scatter(strokebmismoke, x="bmi", y="avg_glucose_level", color="smoking_status", size="age", size_max=30,
          hover_name="gender", facet_col="smoking_status",title="Plot of Body Mass Index and average glucose level with respect to marital status and age")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'# your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig4, filename = '5', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot5():
    # Loading 
    fig5=px.violin(df2, y="age", x="stroke", color="gender", box=True, points="all",title="Distribution of stoke/no stroke: shows outliers and average value of age difference.")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '6', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot6():
    # Loading 
    fig5=px.histogram(strokebmi, x="bmi", y="age", histfunc="sum", color="gender")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'# your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '7', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot7():
    # Loading 
    fig5= px.box(df2, x="gender", y="bmi", color="stroke", notched=True,title="Comparison of BMI of stroke/no stroke. ")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '8', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot8():
    # Loading 
    fig5=  px.bar(stroke, x='work_type',y='age', title='Count based on work type(can see age) of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '9', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot9():
    # Loading 
    fig5=  px.bar(strokebmi, x='gender',y='bmi', title='Count based on Body Mass Index(can see gender) of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '10', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot10():
    # Loading 
    fig5= px.bar(stroke, x='Residence_type',y='age',title='Count based on Residence(can see age) of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '11', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot11():
    # Loading 
    fig5=px.bar(strokesmoke, x='smoking_status',y='age',title='Count based on Smoking Status(can see age) of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '12', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot12():
    # Loading 
    fig5=px.bar(stroke, x='gender',y='avg_glucose_level',title='Count based on Average Glucose level(can see gender) of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '13', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot13():
    # Loading 
    fig5=px.bar(strokebmi, x="gender", y="bmi", color='ever_married',title='Count based on Marital Status(can see gender) and BMI of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '14', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot14():
    # Loading 
    fig5= px.bar(strokebmismoke, x="smoking_status", y="avg_glucose_level", color='gender',title='Count based on Smoking Status(can see Gender) and Average Glucose level of those who had strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '15', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot15():
    # Loading 
    fig5 = px.bar(strokebmi, x="smoking_status", y="age", color='work_type', barmode='group',
             height=400,title="Distribution of people with stroke based on smoking status and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '16', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot16():
    # Loading 
    fig5= px.bar(strokebmi, x="gender", y="avg_glucose_level", color='work_type', barmode='group',
             height=400,title="Distribution of people with stroke based on gender and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '17', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot17():
    # Loading 
    fig5= px.bar(strokebmi, x="Residence_type", y="bmi", color='work_type', barmode='group',
             height=400,title="Distribution of people with stroke based on Residence and work type")
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '18', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot18():
    # Loading 
    fig5= px.pie(df2, names='stroke', title='Percentage of those who suffered from strokes')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '19', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot19():
    # Loading 
    stroke1=strokesmoke[strokesmoke['hypertension']==1]
    fig5= px.pie(stroke1, names='smoking_status', title='Percentage of those who suffered from strokes and had hypertension')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '20', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot20():
    stroke1=strokesmoke[strokesmoke['heart_disease']==1]
    fig5= px.pie(stroke1, names='smoking_status', title='Percentage of those who suffered from strokes and had heart disease')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '21', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot21():
    # Loading 
    fig5= px.pie(stroke,values='hypertension', names='work_type', title='Percentage of those who suffered from strokes based on worktype and had hypertension')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '22', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1

def plot22():
    # Loading 
    fig5 = px.pie(stroke,values='heart_disease', names='work_type', title='Percentage of those who suffered from strokes based on worktype and had heart disease')
    username = 'namma' # your username
    api_key = 'JHD6VUwDyNogOGIstu12'
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    url=py.plot(fig5, filename = '23', auto_open=False)
    url=url.replace("plotly.com","plot.ly")
    #return url
    iframe1=tls.get_embed(url)
    return iframe1


