# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct)
dct.pop('key1')  # removes key1 item
print(dct)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # removes the last item
print(dct)
del dct['key2']  # removes key2 item
print(dct)

# .pop .popitem removes key too. one item = key + value

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# person.pop('first_name')        # Removes the firstname item
# person.popitem()                # Removes the address item
# del person['is_married']        # Removes the is_married item

items = person.items()
print(type(items), items)
keys = person.keys()
values = person.values()
print(type(keys), keys)
print(type(values), values)

dog = {}  # dog = dict()
print(type(dog), dog)
dog['name'] = 'tommy'
dog['breed'] = 'labrador'
dog['legs'] = 23
dog['age'] = 23373

print(dog)
print("========================="*3, "\n")

student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'gender': 'gay',
    'age': 250,
    'country': 'Finland',
    'city': 'Boobiland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(len(student))
print(type(student['skills']), len(student['skills']))
values = student['skills']
print(type(values))
student['skills'].append('Latex')
print(type(student['skills']), len(student['skills']))

keys = list(student.keys())
values = list(student.values())
print(type(keys), keys)
print(type(values), values)

items = student.items()
print(items)
print("========================="*3, "\n")


student.pop('gender')
print(student)
student.popitem()
print(student)

del student
print(student) # NameError: name 'student' is not defined