age = int(input("Enter your age: "))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need {} more years to learn to drive'.format(18 - age))

print("========================="*3, "\n")

my_age = 22
your_age = int(input("Enter your age: "))

if your_age > my_age:
    if (your_age - my_age > 1):
        print("You are {} years older than me.".format(your_age - my_age))
    else:
        print("You are 1 year older than me")
elif your_age == my_age:
    print("You and I are of same age.")
else:
    if (my_age - your_age > 1):
        print("I am {} years older than you".format(my_age - your_age))
    else:
        print("I am 1 year older than you")

print("========================="*3, "\n")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print("{} is greater than {}".format(a, b))
elif a < b:
    print("{} is greater than {}".format(b, a))
else:
    print("{} and {} are same".format(a, b))

print("========================="*3, "\n")

mark = int(input("Enter your marks: "))
if mark >= 90 and mark <= 100:
    print("A")
elif mark >= 70 and mark <= 89:
    print("B")
elif mark >= 60 and mark <= 69:
    print("C")
elif mark >= 50 and mark <= 59:
    print("D")
elif mark >= 0 and mark <= 49:
    print("F")
else:
    print("Invalid mark")

Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

month = input("Enter month: ")

if month in Autumn:
    print("This is Autumn season.")
elif month in Winter:
    print("This is Winter season.")
elif month in Spring:
    print("This is Spring season.")
elif month in Summer:
    print("This is Summer season.")
else:
    print("Enter valid month.")


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exist in the list.")
else:
    fruits.append(fruit)
    print(fruits)
print("========================="*3, "\n")


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

print('skills' in person)

if 'skills' in person:
    if 'Python' in person['skills']:
        print("This person has python skills.")
    else: print("This person has skills but not python skill")
else :
    print("This person doesn't has any skills.")

if len(person['skills']) == 2 and (lang in person['skills'] for lang in ['JavaScript', 'React']):
    print('He is a front end developer')
elif (lang in person['skills'] for lang in['Node', 'React', 'MongoDB']) :
    print('He is a fullstack developer')
elif (lang in person['skills'] for lang in['Node', 'Python', 'MongoDB']):
    print('He is a backend developer')
else:
    print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married.'.format(person['first_name'], person['last_name'], person['country']))