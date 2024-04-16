# 'Day 2: 30 days of python programming'

first_name = "Jyoti"
last_name = "Sahoo"
full_name = "Jyoti Suman Sahoo"
country = "India"
city = "Paradeep"
age = 22
year = 2024
is_married = False
is_true = False
is_light_on = True
first_name1, middle_name1, last_name1 = "Jyoti", "Suman", "Sahoo"

# ========================================================================

print(type(first_name))
print(type(age))
print(type(year))
print(type(is_married))
print(len(full_name))
print(len(first_name) > len(last_name))

# ========================================================================

print("====================================================================")

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * (radius**2)
circum_of_circle = 2 * 3.14 * 30
print("Area: ", area_of_circle, " Circumference: ", circum_of_circle)

radius = int(input("Enter radius of the circle: "))
area_of_circle = 3.14 * (radius ** 2)
print("Area of the circle: ", area_of_circle)

# ========================================================================

help('keywords')