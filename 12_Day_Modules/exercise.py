import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge! in {}'.format(sys.argv[1], sys.argv[2], sys.argv[0]))

print(sys.maxsize)
print(sys.version)
print(sys.path)

from math import pi as  PI
print(PI) # 3.141592653589793

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

print("========================="*3, "\n")

def random_user_id():
    possible_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    LEN = len(possible_characters)
    userId = ''
    for i in range(6):
        flag = randint(0, LEN-1)
        userId += possible_characters[flag]

    return userId

print(random_user_id())

def user_id_gen_by_user():
    possible_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    LEN = len(possible_characters)

    m = int(input("Number of characters: "))
    n = int(input("Number of IDs: "))

    userIds = []

    for i in range(n):
        userId = ''
        for j in range(m):
            flag = randint(0, LEN-1)
            userId += possible_characters[flag]

        userIds.append(userId)

    return userIds

# print(user_id_gen_by_user())

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    res = f'rgb({r},{g},{b})'
    return res

print(rgb_color_gen())

print("========================="*3, "\n")
from random import choice
def hex_color_gen():
    chars = '1234567890abcdef'
    color_code = '#'
    for i in range(6):
        color_code += choice(chars)

    return color_code

def generate_colors(type, cnt):
    my_list = []
    for i in range(cnt):
        my_list.append(rgb_color_gen() if type == 'rgb' else hex_color_gen())

    print(my_list)

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

print("========================="*3, "\n")

def shuffle_list(my_list):
    n = len(my_list)
    new_list = []
    done = set()
    for i in range(n):
        randInd = randint(0, n-1)
        while randInd in done:
            randInd = randint(0, n-1)
        done.add(randInd)
        new_list.append(my_list[randInd])

    return new_list


import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7]
fisher_yates_shuffle(original_list)
print("Shuffled List:", original_list)

'''
Sure, I'll implement a custom shuffling algorithm without using `random.shuffle` and then discuss its time and space complexities. Let's start with a simple shuffling algorithm called the Fisher-Yates shuffle.

### Fisher-Yates Shuffle Algorithm:

#### Description:
The Fisher-Yates shuffle algorithm shuffles an array by iteratively selecting a random element from the unshuffled part of the array and swapping it with the last unshuffled element.

#### Time Complexity:
- The time complexity of the Fisher-Yates shuffle algorithm is O(n), where n is the number of elements in the array.

#### Space Complexity:
- The space complexity of the Fisher-Yates shuffle algorithm is O(1) because it performs in-place swapping without using any additional data structures.

#### Code Implementation:
```python
import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7]
fisher_yates_shuffle(original_list)
print("Shuffled List:", original_list)
```

### Comparison with Other Algorithms:
1. **Fisher-Yates Shuffle**:
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - In-place shuffling algorithm.
   - Uniformly shuffles the array.

2. **Knuth Shuffle** (a variation of Fisher-Yates):
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Similar to Fisher-Yates but swaps the current element with a randomly chosen element from the entire array.

3. **Durstenfeld Shuffle** (another variation of Fisher-Yates):
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Similar to Fisher-Yates but starts from the beginning of the array and iterates towards the end, swapping each element with a randomly chosen element from the unshuffled part of the array.

All three of these algorithms are efficient and produce uniformly random permutations. Fisher-Yates is commonly used due to its simplicity and effectiveness. The Knuth Shuffle and Durstenfeld Shuffle offer variations that might be preferred depending on specific requirements or constraints.

In the Fisher-Yates shuffle algorithm, the loop iterates backwards from `n - 1` to `0` rather than from `n` to `-1` for correctness and efficiency reasons.

Let's break down why this is the case:

1. **Correctness**:
   - In the Fisher-Yates shuffle algorithm, for each iteration `i`, we select a random index `j` from the range `[0, i]` inclusive.
   - If we iterate from `n` to `-1`, the range would be `[n, -1]`, which includes `n` but excludes `-1`. This means that `i` would take values from `n` down to `1`, and the range for selecting `j` would be `[0, n-1]`, which is correct.
   - However, when `i` becomes `0`, the range for selecting `j` would be `[0, -1]`, which doesn't make sense. We want to include the first element of the array in the range for selecting `j`.
   
2. **Efficiency**:
   - The loop iteration `for i in range(n - 1, 0, -1)` ensures that we start from the last element of the array and move towards the first element. This aligns well with the idea of swapping elements in-place while shuffling.
   - Iterating from `n - 1` down to `0` allows us to effectively shuffle the array without needing any extra logic to handle special cases at the beginning or end of the loop.

Therefore, iterating from `n - 1` down to `0` ensures both correctness and efficiency in the Fisher-Yates shuffle algorithm.
    
'''

import string
my_list = list(string.ascii_uppercase)
print(my_list)
print(shuffle_list(my_list))

def seven_random_digits():
    my_nums = []
    for i in range(7):
        randInt = randint(0,9)
        while randInt in my_nums:
            randInt = randint(0, 9)
        my_nums.append(randInt)
    
    return my_nums

print(seven_random_digits())
