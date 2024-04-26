# syntax
# Set stores data in sorted order ?? but why the order changes every time I print the set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument. tuples too
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

removed_item = fruits.pop()
print(removed_item)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print("========================="*3, "\n")

it_companies = set()
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Apple', 'Microsoft', 'Meta', 'Google'])
print(it_companies)

removed_item = it_companies.pop()
print(removed_item)

discarded_item = it_companies.discard('Jio')
print(discarded_item)

# it_companies.remove('Apple')

A = {0, 1, 7, 3, 4}
B = {3, 9, 4, 5, 7}

c = A.intersection(B)
print(c)

print(A.issubset(B))
print(A.isdisjoint(B))

c = A.union(B)
print(A)
print(B)
print(c)

A.update(B)
print(A)
print(B)

B.update(A)

print(A.symmetric_difference(B))
del A, B

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_st = set(ages)
print(len(ages))
print(len(ages_st))

sentence = "I am a teacher and I love to inspire and teach people."
lt = sentence.split()
print(lt)
print(len(lt))
st = set(lt)
print(st)
print(len(st))