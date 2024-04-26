language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

for i in range(5, 10):
    print(i)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i+=1

print("========================="*3, "\n")

for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

for i in range(1, 8):
    print("#"*i)

for i in range(8):
    print("# "*8)

for i in range(11):
    print(f'{i} x {i} = {i*i}')

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

for skill in skills:
    print(skill)

for i in range(101):
    if i % 2 == 0 :
        print(i)
        
for i in range(101):
    if i % 2 != 0 :
        print(i)

sum = 0
for i in range(101):
    sum += i

print(f'The sum of all numbers is {sum}')

sum_e = 0
sum_o = 0
for i in range(101):
    if i%2 == 0:
        sum_e += i
    else:
        sum_o += i

print(f'The sum of all even numbers is {sum_e} and odd numbers is {sum_o}')

# from data import countries

# print(countries.countries[0])

file_path = './data/countries.py'

# Open the Python file for reading
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Evaluate the file contents as Python code
exec(file_contents)

countries = countries
# Now, items_list will contain the list from the file
print(type(countries))

for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']

for items in reversed(fruits):
    print(items)

for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

print(fruits)

print("========================="*3, "\n")

# file_path = './data/countries-data.py'

# import json

# with open(file_path, 'r') as file:
#     data = json.loads(file.read())

# all_languages = [language for country in data for language in country['languages']]

# total_languages = len(set(all_languages))
# print("Total Languages: ", total_languages)

# from collections import Counter

# language_counter = Counter(all_languages)
# top_10_spoken_languages = language_counter.most_common(10)

# print('Ten most spoken languages: ', top_10_spoken_languages)

# # Ten most populated countries
# top_10_populated_countries = sorted(data, key=lambda x: x['population'], reverse=True)[:10]

# print("\nTen most populated countries:", top_10_populated_countries)

import json

# Read the data from countries-data.py
with open('./data/countries-data.py', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

# Total number of languages in the data
all_languages = [language for country in data for language in country['languages']]
total_languages = len(set(all_languages))

print("Total number of languages in the data:", total_languages)

# Ten most spoken languages
from collections import Counter

language_counter = Counter(all_languages)
top_10_spoken_languages = language_counter.most_common(10)

print("\nTen most spoken languages:")
for language, count in top_10_spoken_languages:
    print(language, "-", count)

# Ten most populated countries
top_10_populated_countries = sorted(data, key=lambda x: x['population'], reverse=True)[:10]

print("\nTen most populated countries:")
for country in top_10_populated_countries:
    print(country['name'], "-", country['population'])
