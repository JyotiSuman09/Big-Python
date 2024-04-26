'''
All the fuss about not able to access folders, files outside the script folder.!!
Nigga check your current working dir i.e. from which dir you run your script. Interpreter is running from that dir, so you should specify relative path w.r.t that dir!!!
'''

from collections import Counter
import xml.etree.ElementTree as ET
import csv
import os
import json
import re
import csv

print(os.getcwd())
script_dir = os.path.dirname(__file__)
print(script_dir)
f = open('./files/reading_file_example.txt')
txt = f.read(12)
print(type(txt))
print(txt)
line = f.readline()
print(type(line))
print(line)
line = f.readline()
print(type(line))
print(line)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
# indent could be 2, 4, 8. It beautifies the json
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)

with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

with open('./files/csv_example.csv') as f:
    # w use, reader method to read csv
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


def count_words_lines(file_path):
    line_count = 0
    word_count = 0
    try:
        with open(file_path, 'r') as f:
            # text = f.read()
            # print(text)
            for line in f:
                line_count += 1
                words = line.split()
                word_count += len(words)
    except Exception as e:
        print(e)

    print(word_count, line_count)


def cleaned_word_line_count(file_path):
    line_count = 0
    word_count = 0
    try:
        with open(file_path, 'r') as f:
            # text = f.read()
            # print(text)
            for line in f:
                line_count += 1
                line = re.sub(r'[^\w\s]', '', line)
                words = line.split()
                word_count += len(words)
    except Exception as e:
        print(e)

    print('cleaned:', word_count, line_count)


count_words_lines('./data/obama_speech.txt')
cleaned_word_line_count('./data/obama_speech.txt')

count_words_lines('./data/michelle_obama_speech.txt')
cleaned_word_line_count('./data/michelle_obama_speech.txt')

count_words_lines('./data/donald_speech.txt')
cleaned_word_line_count('./data/donald_speech.txt')

count_words_lines('./data/melina_trump_speech.txt')
cleaned_word_line_count('./data/melina_trump_speech.txt')

print("========================="*3, "\n")

'''
`json.load()` and `json.loads()` are both functions provided by the `json` module in Python for working with JSON data, but they serve different purposes:

1. **json.load()**: This function is used to load JSON data from a file-like object (e.g., file object, string buffer). It takes a file object or a file-like object and reads the JSON data from it. It parses the JSON data and returns a Python data structure (typically a dictionary or a list, depending on the JSON data). 

   Example:
   ```python
   import json

   with open('data.json', 'r') as f:
       data = json.load(f)
   ```

2. **json.loads()**: This function is used to load JSON data from a string. It takes a JSON-formatted string as input and parses it, converting it into a Python data structure.

   Example:
   ```python
   import json

   json_string = '{"name": "John", "age": 30, "city": "New York"}'
   data = json.loads(json_string)
   ```

In summary:
- `json.load()` is used when you have JSON data stored in a file or a file-like object, such as `io.StringIO`.
- `json.loads()` is used when you have JSON data stored as a string.

'''


def most_spoken_languages(file_path, count):
    with open(file_path, 'r', encoding='utf-8') as file:
        # data = file.read()
        # json_data = json.loads(data)
        # print(json_data[:2])
        countries = json.load(file)
        # print(json_data[:2])
        all_languages = [language for country in countries for language in country['languages']]
        language_count = Counter(all_languages)
        most_spoken_languages = language_count.most_common(count)
        most_spoken_languages = [(count, name) for name, count in most_spoken_languages]
        print("Most spoken languages: \n", most_spoken_languages)

def most_populated_countries(filepath, count):
    with open(filepath, encoding='utf-8') as file:
        countries = json.load(file)
        # print(countries[:1])
        sorted_data = sorted(countries, key=lambda x:x['population'], reverse=True)
        output = [{'country': country['name'], 'population': country['population']} for country in sorted_data]
        print(output[:count])

most_spoken_languages('./data/countries_data.json', 3)
most_spoken_languages('./data/countries_data.json', 10)

most_populated_countries('./data/countries_data.json', 3)
most_populated_countries('./data/countries_data.json', 10)

print("========================="*3, "\n")

def list_emails(file_path):
    email_list = []
    email_regex = r'From: (\S+@\S+)'
    with open(file_path) as file:
        for line in file:
            matches = re.findall(email_regex, line)
            email_list.extend(matches)

    for email in email_list:
        print(email)

list_emails('./data/email_exchanges.txt')
# list_emails('./data/email_exchanges_big.txt')

def find_most_common_words(file, count):
    all_words = []
    with open(file) as f:
        for line in f:
            words = line.split()
            all_words.extend(words)
    result = Counter(all_words)
    result = result.most_common(count)
    result = [(cnt, word) for word, cnt in result]
    print(result)

find_most_common_words('./data/obama_speech.txt', 5)
find_most_common_words('./data/michelle_obama_speech.txt', 5)
find_most_common_words('./data/donald_speech.txt', 5)
find_most_common_words('./data/melina_trump_speech.txt', 5)
find_most_common_words('./data/romeo_and_juliet.txt', 10)

def count_keywords(file_path, keyword):
    count = 0
    try:
        with open(file_path) as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                row_text = ' '.join(row)
                if keyword.lower() in row_text.lower():
                    count += 1
    except FileNotFoundError:
        print('File not found.')

    print(count)
    return count

csv_path = './data/hacker_news.csv'
count_keywords(csv_path, 'Python')
count_keywords(csv_path, 'JavaScript')
count_keywords(csv_path, 'Java')

def present_but_not(file_path, keyword, notKeyword):
    count = 0
    try:
        with open(file_path) as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                row_text = ' '.join(row)
                if keyword.lower() in row_text.lower() and notKeyword.lower() not in row_text.lower():
                    count += 1
    except FileNotFoundError:
        print('File not found.')

    print(count)
    return count

java_count = count_keywords(csv_path, 'Java') - count_keywords(csv_path, 'JavaScript')
print(java_count)

present_but_not(csv_path, 'java', 'javascript')