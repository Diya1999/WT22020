from flask import Flask, jsonify, request
from flask_cors import CORS

DATA = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#used inAddData.vue
@app.route('/addData', methods=['POST'])
def addData():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    #this is in the form of a dictionary, need to process it and add to data file 
    response_object['message'] = 'Record added!'

    #if id already exists,
    #response_object['message'] = 'ID already present!!'
    return jsonify(response_object)
  #  return jsonify('pong!')

#used in AddData.vue
@app.route('/getEntry', methods=['POST'])
def getEntry():
    post_data = request.get_json()
    print(post_data)
    #this is in the form of a dictionary, need to process it and look for particular entry with the given id 
    #dummy response onject that is hardcoded. should be an equivalent dictionary of the row with given id
    response_object ={ 'id':123,'age':10,'stroke':0,'work_type':'children'}
    #returns back success status with Data added
    return jsonify(response_object)
  #  return jsonify('pong!')

@app.route('/delEntry/<id>', methods=['DELETE'])
def delete_task(id):
    #checking for the entry with that id, here tasks represnt each row of csv
    #task = [task for task in tasks if task['id'] == task_id]
    print(id)
    #task =''
    if len(task) == 0:
        return jsonify({'message': "No such ID!!"})
        #abort(404)
    #remove particular row from csv  if found 
    #tasks.remove(task)
    return jsonify({'message': "Deleted successfully!"})

if __name__ == '__main__':
    app.run()