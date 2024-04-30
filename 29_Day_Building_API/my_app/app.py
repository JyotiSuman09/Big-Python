import os
import json
import pymongo
from flask import Flask,  Response, jsonify, request
from bson import json_util, objectid
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello</h1>'


@app.route('/api/v1.0/students', methods=['GET'])
def students():
    student_list = [
        {
            'name': 'Asabeneh',
            'country': 'Finland',
            'city': 'Helsinki',
            'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
        },
        {
            'name': 'David',
            'country': 'UK',
            'city': 'London',
            'skills': ['Python', 'MongoDB']
        },
        {
            'name': 'John',
            'country': 'Sweden',
            'city': 'Stockholm',
            'skills': ['Java', 'C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


# Connecting mongoDB
MONGODB_URI = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']


@app.route('/api/v2.0/students', methods=['GET'])
def get_students():
    students = list(db.students.find())  # Convert cursor to list of documents
    # Convert ObjectId to string for JSON serialization
    for student in students:
        student['_id'] = str(student['_id'])
    # Use bson.json_util.dumps to handle ObjectId serialization
    return jsonify(json.loads(json_util.dumps(students)))

    students_list = list(db.students.find())
    for student in students_list:
        student['_id'] = str(student['_id'])
    return Response(json.dumps(students_list), mimetype='application/json')


@app.route('/api/v2.0/students/<id>', methods=['GET'])
def get_by_id(id):
    obj_id = objectid.ObjectId(id)

    # Find student by ObjectId
    # student = db.students.find({'_id': obj_id})
    student = db.students.find_one({'_id': obj_id})

    # If student is not found, return an appropriate response
    if student is None:
        return Response(json.dumps({'error': 'Student not found'}), mimetype='application/json')

    # Convert ObjectId to string for JSON serialization
    student['_id'] = str(student['_id'])

    # Return the student data as JSON response
    return Response(json.dumps(student), mimetype='application/json')


@app.route('/api/v2.0/students', methods = ['POST'])
def create_student ():

    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return

@app.route('/api/v2.0/students/<id>', methods = ['PUT']) # this decorator create the home route
def update_student (id):
    query = {"_id":objectid.ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    return Response(json.dumps({"result":"a new student has been created"}), mimetype='application/json')

@app.route('/api/v2.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":objectid.ObjectId(id)})
    return Response(json.dumps({"result":"The student has been deleted"}), mimetype='application/json')


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
