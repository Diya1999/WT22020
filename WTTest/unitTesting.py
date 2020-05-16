from app import app
import unittest 
import os
import json
import warnings
warnings.filterwarnings("ignore")
import sys
sys.tracebacklimit = 0

class BasicTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def addData(self,id1, gender, age, hypertension, heart_disease,  ever_married, work_type, Residence_type, avg_glucose_level,bmi, smoking_status, stroke):
        #print(id1,gender,hypertension,heart_disease,smoking_status,ever_married,bmi,avg_glucose_level,stroke,age,work_type,Residence_type)
        info={'id':id1, 'gender': gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease, 'ever_married': ever_married, 'work_type': work_type, 'Residence_type': Residence_type, 'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status, 'stroke':stroke}
        return self.app.post('/addData',data=json.dumps(info), follow_redirects=True,mimetype='application/json')

    def deleteData(self,id1):
        #print(id1,gender,hypertension,heart_disease,smoking_status,ever_married,bmi,avg_glucose_level,stroke,age,work_type,Residence_type)
        #info={'id':id1}
        return self.app.delete('/delEntry/'+id1, follow_redirects=True,mimetype='application/json')

    def getData(self,id1):
        #print(id1,gender,hypertension,heart_disease,smoking_status,ever_married,bmi,avg_glucose_level,stroke,age,work_type,Residence_type)
        info={'id':id1}
        return self.app.post('/getEntry/<id>',data=json.dumps(info), follow_redirects=True,mimetype='application/json')

    def getCorrImg(self):
        #print(id1,gender,hypertension,heart_disease,smoking_status,ever_married,bmi,avg_glucose_level,stroke,age,work_type,Residence_type)
        return self.app.get('/correlation', follow_redirects=True)
    
    def getPrediction(self,id1, gender, age, hypertension, heart_disease,  ever_married, work_type, Residence_type, avg_glucose_level,bmi, smoking_status):
        info={'id':id1, 'gender': gender, 'age': age, 'hypertension': hypertension, 'heart_disease': heart_disease, 'ever_married': ever_married, 'work_type': work_type, 'Residence_type': Residence_type, 'avg_glucose_level': avg_glucose_level, 'bmi': bmi, 'smoking_status': smoking_status}
        return self.app.post('/predict',data=json.dumps(info), follow_redirects=True,mimetype='application/json')

    #ADD TESTS

    def test_valid_add_data(self):
        print("\n \nTests whether an entry has been added successfully.")
        response = self.addData('12345678956','Male',"21","False","True","True","Private","Urban","34","67","never_smoked","True")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{\n  "message": "Record added!", \n  "status": "success"\n}\n', response.data)

    def test_data_add_exists(self):
        print("\n \nTests whether an entry already exists and if the given case has been taken care of .")
        response = self.addData('30669','Male',"21","False","True","True","Private","Urban","34","67","never_smoked","True")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{\n  "message": "ID already present!!"\n}\n', response.data)

    def test_data_add_invalid(self):
        print("\n \nTests whether an id is invalid(character instead of digit).")
        response = self.addData("kjhg","Male","21","False","True","True","Private","Urban","34","67","never_smoked","True")
        self.assertEqual(response.status_code, 200)
        #print(response.status_code)
        #print(response.data)
        self.assertIn(b'{\n  "message": "ID is invalid. Should be number!!"\n}\n', response.data)
        
    #DELETE TEST

    def test_valid_delete_exists(self):
        print("\n \nTests whether an entry is successfully deleted.")
        response = self.deleteData('1')
        self.assertEqual(response.status_code, 200)
        #print(response.data)
        self.assertIn(b'{\n  "message": "Deleted successfully!"\n}\n', response.data)
    
    def test_invalid_delete_exists(self):
        print("\n \nTests whether an id exists for deletion.")
        response = self.deleteData('198765467')
        self.assertEqual(response.status_code, 200)
        #print(response.data)
        self.assertIn(b'{\n  "message": "No such ID!!"\n}\n', response.data)
    
    def test_valid_delete_missing(self):
        print("\n \nTests whether an id is missing and the case is taken care of.")
        response = self.deleteData(' ')
        self.assertEqual(response.status_code, 200)
        print(response.data)
        #self.assertIn(b'{\n  "age": 80, \n  "gender": "Female", \n  "id": 1, \n  "strokes": 0\n}\n', response.data)
       
    #GET ENTRY

    def test_invalid_entry(self):
        print("\n \n Tests case for an invalid id for retrieval of data.")
        response = self.getData('1234567890')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{\n  "Error": "No such ID"\n}\n', response.data)
        

    def test_valid_entry(self):
        print("\n \n Tests whether an existing entry is successfully retrieved.")
        response = self.getData('1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{\n  "age": 80, \n  "gender": "Female", \n  "id": 1, \n  "strokes": 0\n}\n', response.data)

    #IMAGE

    def test_valid_image(self):
        print("\n \n Tests case for successful image retrieval")
        response = self.getCorrImg()
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'{\n  "age": 80, \n  "gender": "Female", \n  "id": 1, \n  "strokes": 0\n}\n', response.data)

    #PREDICTION

    def test_prediction(self):
        print("\n \n Tests case for valid prediction")
        response = self.getPrediction("1","Male","21","False","True","True","Private","Urban","34","67","never_smoked")
        self.assertEqual(response.status_code, 200)
        #print(response.status_code)
        #print(response.data)
        self.assertIn(b'"NO STROKE"\n', response.data)

    def test_prediction_no_id(self):
        print("\n \n Tests case for no entry of id for prediction.")
        response = self.getPrediction(" ","Male","21","False","True","True","Private","Urban","34","67","never_smoked")
        self.assertEqual(response.status_code, 200)
        #print(response.status_code)
        #print(response.data)
        self.assertIn(b'"NO STROKE"\n', response.data)
    

    
    

    

