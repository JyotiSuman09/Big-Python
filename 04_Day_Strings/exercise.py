first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

print('In every programming language it starts with \"Hello, World!\"')

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formatted_string = 'The following are python libraries:%s' % (python_libraries)
print(formatted_string)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge[16])
print(challenge.count('y', 7, 14)) # 1,  end= is exclusive
print(challenge.count('th')) # 2`

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = " "
result = result.join(web_tech)
print(len(result)) # 'HTML CSS JavaScript React'


challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

print("========================="*3)
result = 'Thirty' + space + 'Days' + space + 'Of' + space + 'Python'
print(result)

print("========================="*3)
company = 'Coding For All'
print(company)

print("========================="*3)
print(len(company))

print("========================="*3)
print(company.upper())
print(company.lower())
print("Capitalize: ", company.capitalize())
print("Title: ", company.title())
print("Swapcase: ", company.swapcase())
print(company.split(' ')[0])

print("========================="*3)
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.index('Coding'))
print(company.rindex('Coding'))

print("========================="*3)
company2 = company.replace('Coding', 'Python')
print(company)
print(company2)
str1 = "Python for Everyone"
str2 = str1.replace("Everyone", "All")
print(str1)
print(str2)


print("========================="*3)
comp_list = company.split()
print(comp_list)
print(type(comp_list))

company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
comp_list = company.split()
print(comp_list)
print(type(comp_list))

print("========================="*3)
str1 = "Coding For All"
print(str1[0])
print(str1[10])

print("========================="*3)
str1 = "Python For Everyone"
words = str1.split()
acronym = ''

for word in words:
    acronym += word[0]

print(acronym)

str2 = "Coding For All"
words = str2.split()
acronym = ''

for word in words:
    acronym += word[0]

print(acronym)

print("========================="*3)
print(str2.index('C'))
print(str2.index('F'))
print(str2.rfind('l'))
print(str2.startswith('Coding'))
print(str2.endswith('Coding'))
stuff = '   Coding For All      '
print("Before formatting: ", stuff)
formatted_stuff = stuff.strip()
print("After formatting: ", formatted_stuff)


print("========================="*3)
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence.find('because'))
print(sentence.rfind('because'))
start_index = sentence.find('because because because')
end_index = start_index + len('because because because')
phrase = sentence[start_index:end_index]
print("Sliced phrase:", phrase)

print("========================="*3)
str1 = '30DaysOfPython'
str2 = 'thirty_days_of_python'
print(str1.isidentifier())
print(str2.isidentifier())

print("========================="*3)
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string = '# '.join(libraries)
print(string)

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

print("radius = {}\narea = {} * radius ** {}\nThe area of a circle with radius {} is {} meters square".format(10, 3.14, 2, 10, 314))
radius = 10
area = 3.14 * radius ** 2

# Using string formatting to display the result
print("The area of a circle with radius {} is {:.2f} meters square.".format(radius, area))


a = 8
b = 6

# Perform arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b

# Using string formatting to display the results
print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subtraction))
print("{} * {} = {}".format(a, b, multiplication))
print("{} / {} = {:.2f}".format(a, b, division))
print("{} % {} = {}".format(a, b, modulus))
print("{} // {} = {}".format(a, b, floor_division))
print("{} ** {} = {}".format(a, b, exponentiation))
