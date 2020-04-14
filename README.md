# Web Tech II Laboratory - PES University

Analysis and Visualization of Healthcare data

## Description
The website looks into the analysis of stroke related healthcare dataset (Dataset.zip)
Pages:
1. Home Page - The front page through with basic details and navigation to the pages (wt_project/views/Home.vue)
2. Login Page - The page helps Admins to login to their account (Firebase authenticiation) (wt_project/views/Signin.vue)
3. Stats Page - This page has analysis,interactive graphs and visualization of various attributes related to strokes (wt_project/views/STATS.vue)
4. Prediction Page - On entering certain parameters, our ML model will predict the chances of a stroke (wt_project/views/PREDICTIONS.vue)
5. Change Data Page - As the admin, one can add/ delete entries from the dataset (wt_project/views/AddData.vue)

## Front End Framework used:
Vue js + Veutify

## Backend Framework used:
Flask using Python

## Technologies used:

### Periodic Refresh using XHR calls: 
The visualization page automatically gets updated after a periodic interval, hence any change in the dataset would reflect on the interactive graphs as well

### RESTful API calls : 
API's using flask have been used for accessing the backend.
1. Adding entries to the dataset
2. Deleting entries based on ID
3. Predicting strokes based on entries, with resulting confusion matrix
4. Each visualization/ interactive graph is called and set as an iframe in the frontend by calling their respective API

### Intelligent Component:
1. Machine Learning (Desicion Trees) : Used to train the dataset and classify if a particular entry would lead to a stroke or not
2. Data Analytics using EDA and visualization: Understanding the relation between multiple attributes of the dataset and how each overall affect the classification

## Files
1. app.py : Consists of all the APIs
2. wt_project.7z : a compressed version of the folder with the entire frontend written in Vue
3. model1.py : training the model along with predictions
4. not1.py : python files with all visualization

## Contributors

### C Diya - PES1201700246
### Namrata R - PES1201700921
### Chiranth J - PES1201701438


