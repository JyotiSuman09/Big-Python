from bson.objectid import ObjectId
from flask import Flask, render_template
import pymongo
import os  # importing operating system module
MONGODB_URI = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(MONGODB_URI)
# # Creating or opening database
# db = client.thirty_days_of_python
db = client['thirty_days_of_python']

# # Creating students collection and inserting a document
# db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
# print(client.list_database_names())

# students = [
#     {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
#     {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
#     {'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25},
# ]

# for student in students:
#     db.students.insert_one(student)

# db = client['thirty_days_of_python']
# student = db.students.find_one()
# print(student)

# db = client['thirty_days_of_python']
# student = db.students.find_one({'_id':ObjectId('6630bed56cae52488267017c')})
# print(student)

# students = db.students.find()
# for student in students:
#     print(student)

# print(type(students))
# print(students)

# students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
# for student in students:
#     print(student)

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)

# app = Flask(__name__)
# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
