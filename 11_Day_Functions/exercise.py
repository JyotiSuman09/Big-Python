import math


def add_two_numbers(x, y):
    return x + y


def area_of_circle(r):
    return 3.14 * r ** 2


print(area_of_circle(4))


def add_all_numbers(*args):
    total = 0
    for x in args:
        if isinstance(x, (int, float, complex)):
            total += x
        else:
            print(f'{x} is not a number type. Skipping this value.')

    return total


print(add_all_numbers(3, 2, 'hello', 53, 93, '23', 99))


def convert_celsius_to_fahrenheit(c):
    return round((c * (9/5)) + 32, 2)


print(convert_celsius_to_fahrenheit(25))


def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid month, Enter correct month name.'


print(check_season('August'))


def check_slope_pair_of_points(x1, x2, y1, y2):
    if x1 == x2:
        raise ValueError("Cannot calculate slope: The line is vertical.")
    slope = (y2 - y1)/(x2 - x1)
    return slope


# equation of the form ax + by + c = 0
def check_slope_linear_equation(a, b, c):
    if b == 0:
        raise ValueError("Cannot calculate slope: The line is vertical.")

    slope = -a / b
    return slope


def solve_quadratic_eqn(a, b, c):
    D = b**2 - 4*a*c
    if D == 0:
        root1 = -b/(2*a)
        root2 = -b/(2*a)
    elif D > 0:
        root1 = (-b + math.sqrt(D))/(2*a)
        root2 = (-b - math.sqrt(D))/(2*a)
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(abs(D))/(2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    return root1, root2


# Example usage:
a = 1
b = 4
c = 8
root1, root2 = solve_quadratic_eqn(a, b, c)
print("Root 1:", root1)
print("Root 2:", root2)


def print_list(my_list):
    for item in my_list:
        print(item)


def reverse_list(my_list):
    n = len(my_list)
    for i in range(n//2 + 1):
        temp = my_list[i]
        my_list[i] = my_list[n-1-i]
        my_list[n-1-i] = temp
    return my_list


print(reverse_list([1, 2, 3, 4, 5, 6]))
# [6, 5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]


def remove_item(my_list, item):
    del my_list[my_list.index(item)]


my_list = [1, 2, 3, 4, 5, 6]
remove_item(my_list, 3)
print(my_list)


def modify_list(lst):
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]


def modify_integer(num):
    num = num + 1


my_num = 10
modify_integer(my_num)
print(my_num)  # Output: 10

# int object type is immutable while list obj type is mutable in python

print("========================="*3, "\n")


def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(odds, " ", evens)


evens_and_odds(100)


def factorial(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x


print(factorial(5))


def is_empty(parameter):

    if not parameter:
        return True
    else:
        return False


# Example usage
print(is_empty(""))        # Output: True
print(is_empty([]))        # Output: True
print(is_empty({}))        # Output: True
print(is_empty(set()))     # Output: True
print(is_empty(0))         # Output: True
print(is_empty(None))      # Output: True
print(is_empty("Hello"))   # Output: False
print(is_empty([1, 2, 3]))  # Output: False
print(is_empty({1, 2, 3}))  # Output: False


def evaluate(my_list):
    n = len(my_list)
    my_list.sort()
    print(my_list)

    # Mean
    mean = sum(my_list)/n
    print("Mean: ", round(mean, 3))

    # Median
    if n % 2 != 0:
        print("Median: ", my_list[n//2])
    else:
        print("Median: ", sum(my_list[n//2-1: n//2+1])/2)

    # Mode
    frequency = {}
    for item in my_list:
        frequency[item] = frequency.get(item, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    print("Mode(s): ", modes)

    # Range
    print("Range: ", max(my_list) - min(my_list))

    # Variance
    variance = sum((item - mean)**2 for item in my_list) / n
    print("Variance: ", round(variance, 3))

    # Standard Deviation
    print("Standard deviation: ", round(math.sqrt(variance), 3))

evaluate([1, 1, 2, 3, 2, 5, 6, 3])

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

# Example usage
print(isPrime(7))   # Output: True
print(isPrime(11))  # Output: True
print(isPrime(15))  # Output: False

def check_unique(my_list):
    n = len(my_list)
    n2 = len(set(my_list))

    return n == n2

print(check_unique([1, 2, 3, 4, 6]))
print(check_unique([1, 1, 2, 3, 4, 6]))

def check_same_data_type(my_list):
    if not my_list:
        return True
    first_type = type(my_list[0])
    return all(isinstance(item, first_type) for item in my_list)
# The all() function in Python returns True if all elements of the iterable are true (or if the iterable is empty). If any element of the iterable is false, it returns False.

# Example usage
print(check_same_data_type([1, 2, 3]))       # Output: True
print(check_same_data_type([1, 2, "3"]))     # Output: False
print(check_same_data_type(["a", "b", "c"]))  # Output: True

print("\n", "========================="*3, "\n")

def is_valid_variable(variable):
    if not isinstance(variable, str):
        return False
    if not variable:
        return False
    if variable[0].isdigit():
        return False
    return all(c.isalnum() or c == '_' for c in variable)

# Example usage
print(is_valid_variable("variable"))  # Output: True
print(is_valid_variable("123var"))    # Output: False
print(is_valid_variable("var123"))    # Output: True
print(is_valid_variable("var_123"))   # Output: True
print(is_valid_variable("_var"))      # Output: True
print(is_valid_variable(""))          # Output: False
print(is_valid_variable(None))        # Output: False
