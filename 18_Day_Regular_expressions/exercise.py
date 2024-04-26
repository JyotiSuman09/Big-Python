import string
from collections import Counter
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))  # splitting using \n - end of line symbol

print("========================="*3, "\n")

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph.lower())
word_freq = Counter(words)
output = [(freq, word) for word, freq in word_freq.items()]
output.sort(reverse=True)
print(len(output), output)

words = re.findall(r'\b\w+\b', paragraph)
word_freq = Counter(words)
outputA = [(freq, word) for word, freq in word_freq.items()]
outputA.sort(reverse=True)
print(len(outputA), outputA)

A = set(output)
B = set(outputA)
C = (B - A)
D = (A - B)
print(C)
print(D)

print("========================="*3, "\n")

# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20

paragraph = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

reg_exp = r'-?\d+'
points = re.findall(reg_exp, paragraph)
print(points)
sorted_points = sorted([int(x) for x in points])
print(sorted_points)
distance = sorted_points[-1] - sorted_points[0]
print(distance)

# wrong regex as '_' is not a valid python identifier. so replace * with +
identifier_regexp = r'[^0-9]_?[a-zA-Z0-9_]*'
identifier_regexpA = r'[^0-9]_?[a-zA-Z0-9_]+'
identifier_regexpB = r'[^0-9]_?[a-zA-Z0-9_]+$'
identifier_regexpC = r'^[a-zA-Z_][a-zA-Z0-9_]*'
identifier_regexpD = r'^[a-zA-Z_][a-zA-Z0-9_]*$'


def is_valid_variable(variable_name):
    O = bool(re.match(identifier_regexp, variable_name))
    A = bool(re.match(identifier_regexpA, variable_name))
    B = bool(re.match(identifier_regexpB, variable_name))
    C = bool(re.match(identifier_regexpC, variable_name))
    D = bool(re.match(identifier_regexpD, variable_name))
    return (f'{variable_name}: (O, {O}), (A, {A}), (B, {B}), (C, {C}), (D, {D})')


# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))   # True

print("========================="*3, "\n")
print(string.punctuation)

def clean_text(sentence):
    # unwanted_chars = string.punctuation
    unwanted_chars = r'[!@%@$#&;]'
    cleaned_text = re.sub(unwanted_chars, '', sentence)
    return cleaned_text


def most_frequent_words(paragraph):
    word_regex = r'\b\w+\b'
    words = re.findall(word_regex, paragraph)

    word_freq = Counter(words)
    return word_freq.most_common(3)


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
print(most_frequent_words(cleaned_text))

punctuation_pattern = '[' + re.escape(string.punctuation) + ']'
print(punctuation_pattern)