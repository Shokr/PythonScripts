###########################################################################
# Taking Space Separated Multiple Inputs

import datetime
import operator
import os.path
import sys
import time
# Taking Two Integers as input
import timeit
from itertools import repeat
from operator import itemgetter
from os import path

import numpy as np

a, b = map(int, input().split())
print("a:", a)
print("b:", b)

# Taking a List as input
arr = list(map(int, input().split()))
print("Input List:", arr)
###########################################################################

###########################################################################
# Accessing Index and Value at the Same Time

arr = [2, 4, 6, 3, 8, 10]

for index, value in enumerate(arr):
    print(f"At Index {index} The Value Is -> {value}")

"""Output
At Index 0 The Value Is -> 2
At Index 1 The Value Is -> 4
At Index 2 The Value Is -> 6
At Index 3 The Value Is -> 3
At Index 4 The Value Is -> 8
At Index 5 The Value Is -> 10
"""
###########################################################################

###########################################################################
# Check Memory Usage


a = 20
print(sys.getsizeof(a))
###########################################################################

###########################################################################
#  Prints the Unique ID of a Variable

x = 100
print(id(x))
###########################################################################

###########################################################################
#  Check for an Anagram
"""An anagram is a word that is formed by rearranging the letters of a different word,
using all the original letters exactly once."""


def check_anagram(first_word, second_word):
    return sorted(first_word) == sorted(second_word)


print(check_anagram("silent", "listen"))  # True
print(check_anagram("ginger", "danger"))  # False
###########################################################################

###########################################################################
# Merging Two Dictionaries

basic_information = {"name": ["karl", "Lary"], "mobile": ["0134567894", "0123456789"]}
academic_information = {"grade": ["A", "B"]}
details = dict()  # Combines Dict

# Dictionary Comprehension Method
details = {
    key: value
    for data in (basic_information, academic_information)
    for key, value in data.items()
}
print(details)

# Dictionary unpacking
details = {**basic_information, **academic_information}
print(details)

# Copy and Update Method
details = basic_information.copy()
details.update(academic_information)
print(details)
###########################################################################

###########################################################################
# Checking if a File Exists

# Brute force Method


def check_for_file():
    print("File exists: ", path.exists("data.txt"))


if __name__ == "__main__":
    check_for_file()

"""
File exists:  False
"""
###########################################################################

###########################################################################
# Square of all numbers in a given range

# METHOD 1

n = 5
squares = list(map(pow, range(1, n + 1), repeat(2)))
print(squares)

# METHOD 2
n = 6
squares = [i ** 2 for i in range(1, n + 1)]
print(squares)


"""Output
  [1, 4, 9, 16, 25]
"""
###########################################################################

###########################################################################
# Converting two lists into a dictionary

list1 = ["karl", "lary", "keera"]
list2 = [28934, 28935, 28936]

# Method 1: zip()
dictt0 = dict(zip(list1, list2))

# Method 2: dictionary comprehension
dictt1 = {key: value for key, value in zip(list1, list2)}

# Method 3: Using a For Loop (Not Recommended)
tuples = zip(list1, list2)
dictt2 = {}
for key, value in tuples:
    if key in dictt2:
        pass
    else:
        dictt2[key] = value
print(dictt0, dictt1, dictt2, sep="\n")
###########################################################################

###########################################################################
# Sorting a List of Strings

list1 = ["Karl", "Larry", "Ana", "Zack"]

# Method 1: sort()
list1.sort()

# Method 2: sorted()
sorted_list = sorted(list1)

# Method 3: Brute Force Method
size = len(list1)
for i in range(size):
    for j in range(size):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)
###########################################################################

###########################################################################
#  Adding Elements of Two Lists

maths = [59, 64, 75, 86]
physics = [78, 98, 56, 56]

# Brute Force Method
list1 = [
    maths[0] + physics[0],
    maths[1] + physics[1],
    maths[2] + physics[2],
    maths[3] + physics[3],
]


# List Comprehension
list1 = [x + y for x, y in zip(maths, physics)]

# Using Maps

all_devices = list(map(operator.add, maths, physics))

# Using Numpy Library

list1 = np.add(maths, physics)

"""Output
[137 162 131 142]
"""
###########################################################################


###########################################################################
# Sorting a List of Dictionaries

dict1 = [
    {"Name": "Karl", "Age": 25},
    {"Name": "Lary", "Age": 39},
    {"Name": "Nina", "Age": 35},
]

# Using sort()
dict1.sort(key=lambda item: item.get("Age"))

# List sorting using itemgetter

f = itemgetter("Name")
dict1.sort(key=f)


# Iterable sorted function
dict1 = sorted(dict1, key=lambda item: item.get("Age"))

"""Output
[{'Age': 25, 'Name': 'Karl'},
 {'Age': 35, 'Name': 'Nina'},
 {'Age': 39, 'Name': 'Lary'}]
"""
###########################################################################

###########################################################################
# Calculating Time of a Shell

# METHOD 1

start = datetime.datetime.now()
"""
CODE
"""
print(datetime.datetime.now() - start)

# METHOD 2

start_time = time.time()
main()
print(f"Total Time To Execute The Code is {(time.time() - start_time)}")

# METHOD 3

code = """
## Code snippet whose execution time is to be measured
[2,6,3,6,7,1,5,72,1].sort()
"""
print(timeit.timeit(stmy=code, number=1000))
###########################################################################

###########################################################################
# Checking For Substrings In a String of List

addresses = [
    "12/45 Elm street",
    "34/56 Clark street",
    "56,77 maple street",
    "17/45 Elm street",
]
street = "Elm street"
for i in addresses:
    if street in i:
        print(i)

"""output
12/45 Elm street
17/45 Elm street
"""
###########################################################################

###########################################################################
# Formatting a String

name = "Abhay"
age = 21

# METHOD 1: Concatenation
print("My name is " + name + ", and I am " + str(age) + " years old.")

# METHOD 2: F-strings (Python 3+)
print(f"My name is {name}, and I am {age} years old")

# METHOD 3: Join
print("".join(["My name is ", name, ", and I am ", str(age), " years old"]))

# METHOD 4: modulus operator
print("My name is %s, and I am %d years old." % (name, age))

# METHOD 5: format(Python 2 and 3)
print("My name is {}, and I am {} years old".format(name, age))
###########################################################################

###########################################################################
# Error Handling

# Example 1
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print(c)
except:
    print("Can't divide with zero")

# Example 2
try:
    # this will throw an exception if the file doesn't exist.
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close()

# Example 3
try:
    fptr = open("data.txt", "r")
    try:
        fptr.write("Hello World!")
    finally:
        fptr.close()
        print("File Closed")
except:
    print("Error")
###########################################################################

###########################################################################
# Most Frequent in a List


def most_frequent(nums):
    return max(set(nums), key=nums.count)


###########################################################################

###########################################################################
# Calculator Without if-else


action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow,
}

print(action["*"](5, 5))  # 25
###########################################################################

###########################################################################
# Chained function call


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


a, b = 9, 6
print((sub if a > b else add)(a, b))
###########################################################################

###########################################################################
# Calculator Without if-else


action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow,
}

print(action["*"](5, 5))  # 25
###########################################################################

###########################################################################
# Swap Values


def swap(a, b):
    return b, a


swap(a, b)
###########################################################################

###########################################################################
# Finding duplicates


def has_duplicates(lst):
    return len(lst) != len(set(lst))


###########################################################################################

###########################################################################################
# Palindrome : is a number or a string that looks the same when it gets reversed.


def is_palindrome(text):
    return text == text[::-1]


###########################################################################################

###########################################################################################
# Scale


def scale(lst, x):
    return [i * x for i in lst]


scale([2, 3, 4], 2)  # call
###########################################################################################

###########################################################################################
# Transpose of a matrix

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [list(i) for i in zip(*a)]
transpose
###########################################################################################
