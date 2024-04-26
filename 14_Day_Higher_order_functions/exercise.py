def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(f, x):
    return f(x)

print(higher_order_function(square, 3))
print(higher_order_function(cube, 3))
print(higher_order_function(absolute, -3))


'''These decorator functions are higher order functions
that take functions as parameters'''

def greeting():
    return 'Welcome to Python'

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


g = uppercase_decorator(greeting)
g = split_string_decorator(g)
print(g())

# OR

# @split_string_decorator
# @uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
# def greeting():           # define function after @
#     return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON

def decorator_with_parameters(function):
    p = 'gae'
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3, p)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country, p):
    print("I am {} {}. I love to teach. {}".format(
        first_name, last_name, p, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

print("========================="*3, "\n")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map - takes a function and an iterable and returns a iterable. performs the function on each item and returns a new list
# filter - takes a boolean return type function and filters the items on that satisfy by the boolean function
# reduce - takes a function and an iterable but returns a single value. It carry out the function on each of the items cumulatively

'''
Let's break down each of these concepts:

### Difference between `map`, `filter`, and `reduce`:

1. **`map`**:
   - `map` applies a given function to each item of an iterable (e.g., a list) and returns a new iterator with the results.
   - It takes two arguments: the function to apply and the iterable to apply it to.
   - Example: `map(lambda x: x**2, [1, 2, 3, 4])` will produce `[1, 4, 9, 16]`, squaring each element of the list.

2. **`filter`**:
   - `filter` applies a given function to each item of an iterable, filtering out the items for which the function returns `False`.
   - It takes two arguments: the function to apply (which should return a boolean) and the iterable to apply it to.
   - Example: `filter(lambda x: x % 2 == 0, [1, 2, 3, 4])` will produce `[2, 4]`, filtering out the odd numbers.

3. **`reduce`**:
   - `reduce` is used to perform a computation on a list and return the result.
   - It takes two arguments: the function to perform the computation and the iterable to apply it to.
   - Example: `from functools import reduce; reduce(lambda x, y: x+y, [1, 2, 3, 4])` will produce `10`, summing all elements of the list.

### Difference between higher-order function, closure, and decorator:

1. **Higher-order function**:
   - A higher-order function is a function that takes one or more functions as arguments or returns a function as its result.
   - Example: `map`, `filter`, and `reduce` are higher-order functions because they take functions as arguments.

2. **Closure**:
   - A closure is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is called even if they are not in scope.
   - Example: A function returning another function that uses variables from the outer function.

3. **Decorator**:
   - A decorator is a function that takes another function as input and extends or modifies its behavior without modifying the function itself.
   - Example: Adding logging, authentication, or caching to a function without changing its code directly.

### Define a `call` function before `map`, `filter`, or `reduce`:

```python
def call(func, iterable):
    return [func(item) for item in iterable]

# Example usage:
result = call(lambda x: x**2, [1, 2, 3, 4])
print(result)
```

### Using `for` loop to print each item:

```python
# Printing each country in the countries list
countries = ['USA', 'Canada', 'Germany']
for country in countries:
    print(country)

# Printing each name in the names list
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# Printing each number in the numbers list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

These `for` loops iterate over each item in the respective lists (`countries`, `names`, and `numbers`) and print them one by one.
'''
print("========================="*3, "\n")

output = map(lambda x: x.upper(), countries)
print(list(output))

output = map(lambda x: x**2, numbers)
print(list(output))

output = map(lambda x: x.upper(), names)
print(list(output))

output = filter(lambda x: 'land' not in x, countries)
print(list(output))

output = filter(lambda x: len(x) != 6, countries)
print(list(output))

output = filter(lambda x: len(x) < 6, countries)
print(list(output))

output = filter(lambda x: x[0] != 'E', countries)
print(list(output))

square = lambda x: x**2
is_even = lambda x: x % 2 == 0
summation = lambda x, y: x + y

from functools import reduce
output = reduce(summation, filter(is_even, map(square, numbers)))
print(output)

def get_string_lists(arr):
    arr = filter(lambda x: isinstance(x, str), arr)
    return list(arr)

arr = numbers + countries
print(arr)
print(get_string_lists(arr))

output = reduce(summation, numbers)
print(output)

sentence = reduce(lambda x, y: f'{x}, {y}', countries[:-1]) + f' and {countries[-1]} are north European countries.'
print(sentence)

from functools import reduce

# Define the list of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Define the function for reducing
concatenate_countries = lambda x, y: x + ', ' + y

# Use reduce to concatenate the countries
concatenated_string = reduce(concatenate_countries, countries)

# Separate the last country and add "and"
if len(countries) > 1:
    last_country = countries[-1]
    concatenated_string = concatenated_string[:-len(last_country)] + 'and ' + last_country

# Format the resulting string
result = concatenated_string + ' are north European countries.'

print(result)

# './module/exercise.py'

import sys, os
print(os.getcwd())
sys.path.append(os.getcwd())

from data.countries import countries

# Now you can use the country_names list in your current file
print(countries)

print("========================="*3, "\n")

def categorize_countries(countries):
    common_patterns = ['land', 'ia', 'island', 'stan']
    categorized_countries = []

    for country in countries:
        for pattern in common_patterns:
            if pattern in country.lower():
                categorized_countries.append(country)
                break

    return categorized_countries

print(reduce(lambda x, y: f'{x}\n{y}', categorize_countries(countries)))

def calc_freq(countries):
    freq = {}

    for country in countries:
        first_letter = country[0].upper()
        if first_letter in freq:
            freq[first_letter] += 1
        else:
            freq[first_letter] = 1
    
    return freq

print(calc_freq(countries))
print("\n".join([f"{letter}: {count}" for letter, count in calc_freq(countries).items()]))

def get_first_ten_countries(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire contents of the file
            file_contents = file.read()
            # Evaluate the contents as Python code
            exec(file_contents, globals())  # Use exec to execute the Python code
            # Extract the 'countries' list from the evaluated code
            countries_list = globals().get('countries', [])
            return countries_list[:10]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    
def get_last_ten_countries(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire contents of the file
            file_contents = file.read()
            # Evaluate the contents as Python code
            exec(file_contents, globals())  # Use exec to execute the Python code
            # Extract the 'countries' list from the evaluated code
            countries_list = globals().get('countries', [])
            return countries_list[-10:]
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []

print(os.getcwd())
print(os.path.exists(os.getcwd() + '/data/countries.py'))
print(os.path.exists('../data/countries.py'))
# print(get_first_ten_countries('./data/countries.js'))

file_path = '../data/countries.py'
file_path = os.getcwd() + '/data/countries.py'
countries = get_first_ten_countries(file_path)
print(countries)

countries = get_last_ten_countries(file_path)
print(countries)

print("========================="*3, "\n")
import json

def by_name_capital_population(countries):
    # Sort countries by name
    sorted_by_name = sorted(countries, key=lambda x: x['name'])

    # Sort countries by capital
    sorted_by_capital = sorted(countries, key=lambda x: x['capital'])

    # Sort countries by population
    sorted_by_population = sorted(countries, key=lambda x: x['population'])

    print("Sorted by name:")
    for country in sorted_by_name[:5]:
        print(country['name'])

    print("\nSorted by capital:")
    for country in sorted_by_capital[:5]:
        print(country['name'] + ': ' + country['capital']) # empty capital value in data so output is empty string

    print("\nSorted by population:")
    for country in sorted_by_population[:5]:
        print(country['name'] + ': ' + str(country['population']))

def most_spoken_language(countries):
    # Extract all languages from the list of dictionaries
    all_languages = [language for country in countries for language in country['languages']]

    # Count the occurrence of each language
    language_count = {language: all_languages.count(language) for language in set(all_languages)}

    # Sort languages by frequency and get the ten most spoken languages
    most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTen most spoken languages:")
    for language, count in most_spoken_languages:
        print(f"{language}: {count}")

def most_populated(countries):
    # Sort countries by population in descending order and get the ten most populated countries
    most_populated_countries = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]

    print("\nTen most populated countries:")
    for country in most_populated_countries:
        print(f"{country['name']}: {country['population']}")


def sort_by_value(file_path, f):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
            # print(countries_data[:1])
            f(countries_data)

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

file_path = os.getcwd() + '/data/countries-data.py'
# Sort countries by name, by capital, by population
sort_by_value(file_path, by_name_capital_population)
print("========================="*3, "\n")

# Sort out the ten most spoken languages by location.
sort_by_value(file_path, most_spoken_language)
print("========================="*3, "\n")

# Sort out the ten most populated countries.
sort_by_value(file_path, most_populated)
# print("========================="*3, "\n")