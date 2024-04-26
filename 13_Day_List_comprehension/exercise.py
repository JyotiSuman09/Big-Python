# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print(numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)


def power(x):
    return lambda n: x ** n


# function power now need 2 arguments to run, in separate rounded brackets
cube = power(2)(3)
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32

print("========================="*3, "\n")

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
output = [i for i in numbers if i <= 0]
print(output)

list_of_list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output = [nums for list_of_lists in list_of_list_of_lists for rows in list_of_lists for nums in rows]
print(output)

output = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(output)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
halo = 'ajidfs'

output = [[country.upper(), country.upper()[:3], capital.upper()]
          for list_of_tuple in countries for country, capital in list_of_tuple]

print(output)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output: [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

output = [{'country': country.upper(), 'city': city.upper()}
          for sublist in countries for country, city in sublist]
print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output: ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

output = [f'{first} {last}' for sublist in names for first, last in sublist]
print(output)


linear_function = lambda x1, y1, x2, y2, slope=True: (y2 - y1) / (x2 - x1) if slope else y1 - ((y2 - y1) / (x2 - x1)) * x1

# Example usage:
# Calculate slope
slope = linear_function(2, 3, 5, 9)
print("Slope:", slope)

# Calculate y-intercept
y_intercept = linear_function(2, 3, 5, 9, slope=False)
print("Y-intercept:", y_intercept)

