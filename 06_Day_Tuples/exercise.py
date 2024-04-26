fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
animal_products = ('Meat', 'Milk', 'Pork', 'Eggs')

my_tuple = ()
brothers = ('dibya', 'subham')
sisters = ('sona', 'guguli')
siblings = brothers + sisters
print(siblings)
print(len(siblings))
my_list = list(siblings)
my_list.append('Akshaya')
my_list.append('Suchitra')
my_family = tuple(my_list)
print(my_family)
siblings = my_family[:-2]
parents = my_family[-2:]
print(type(siblings), siblings)
print(type(parents), parents)

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

middle_index = len(food_stuff_tp) // 2

middle_items = food_stuff_tp[middle_index: middle_index+1] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index-1: middle_index+1]
print(middle_items)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)