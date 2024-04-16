# =========================
age = 22
height = 158.5
ego = 4 + 3j

print(age)
print(height)
print(ego)
# =========================

b = float(input("Enter base: "))
h = float(input("Enter height: "))
print("The area of the triangle is ", 0.5 * b * h)
# =========================

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("The perimeter of the triangle is ", a + b + c)
# =========================

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("The area of the rectangle is ", width * height)
print("The perimeter of the rectangle is ", 2 * (width + length))
# =========================

radius = float(input("Enter radius of the circle: "))
print("The area of the circle is ", 3.14 * radius ** 2)
print("The perimeter of the circle is ", 2 * 3.14 * radius)
# =========================

# eq-> y = 2x - 2


def calculate_slope_intercepts():
    # Eq y = mx + c
    m = 2
    c = -2

    slope = m
    x_intercept = c / (-m)
    y_intercept = c

    return slope, x_intercept, y_intercept

slope, x_cap, y_cap = calculate_slope_intercepts()
print("Slope: ", slope)
print("x-intercept: ", x_cap)
print("y-intercept: ", y_cap)
# =========================

# m = y2-y1/x2-x1
x1, y1 = 2, 2
x2, y2 = 6, 10

distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
slope2 = (y2-y1)/(x2-x1)

print("Slope: ", slope2)
print("Euclidean distance: ", distance)
# =========================

print("slope1" if slope > slope2 else "slope2", " is higher." )
# =========================

# eq-> y = x^2 + 6x + 9
def f(x):
    return x**2 + 6*x + 9

x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for x in x_values:
    print(f"For x={x}, y=", f(0))

import math
def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        alpha = (-b + math.sqrt(D)) / (2*a)
        beta = (-b - math.sqrt(D)) / (2*a)
        return alpha, beta
    elif D == 0:
        alpha = -b / (2*a)
        return alpha, alpha
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(D))/ (2*a)
        alpha = complex(real_part, imaginary_part)
        beta = complex(real_part, -imaginary_part)
        return alpha, beta

alpha, beta = quadratic_roots(1, 6, 9)
print(f"Roots are {alpha} and {beta}")
# =========================

str1 = 'python'
str2 = 'dragon'

len1 = len(str1)
len2 = len(str2)

falsy_comparison = (len1 != len2)
print(f"Length of 'python' is {len1} and 'dragon' is {len2}.")
print("Is the length of 'python' different from the length of 'dragon'?", falsy_comparison)
# =========================

is_present = ('on' in str1) and ('on' in str1)
print("Is 'on' found in both 'python' and 'dragon'?", is_present)
# =========================

sentence = "I hope this course is not full of jargon."
print("Is jargon present? ", ('jargon' in sentence))
# =========================

print("There is no 'on' found in both 'python' and 'dragon'?", ('on' not in str1) and ('on' not in str1))
# =========================

len1_f = float(len1)
len1_s = str(len1_f)
print("Converted string of length in float: ", len1_s)
# =========================

def is_even(num):
    return num % 2 == 0
# =========================

print("Floor division of 7 by 3 is ", 7 // 3)
print("Int converted value of 2.7 is ", int(2.7))
print("Are both same: ", 7//3 == int(2.7))
# =========================

print(f"type of '10' {type('10')} is equal to type of 10 {type(10)}? ", type('10') == type(10))
# =========================

print("Check if int('9.8') is equal to 10 ", int(float('9.8')) == 10)
# =========================

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is ", hours * rate)
# =========================

years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years * 31536000} seconds")
# =========================

# Define the number of rows
num_rows = 5

# Iterate over each row
for i in range(1, num_rows + 1):
    print(i, 1, i, i**2, i**3)

