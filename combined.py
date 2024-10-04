#1) pretty print
# speciality :- debugging in console when unstructured data is given.
import pprint
import json
with open("load.json", "r") as f:
    data = json.load(f)
pprint(data)

#4) "any function" simply tells you if any of the values in an interable object result/ equivalent in/to true
# Speicality:- allows you to write some of the readable code

numbers = [0,1,2,3,4]
print(any(numbers)) #This gives True

num1 = [-1,-2,0, -22]

print(any(num >0 for num in num1)) #gives false

strings = ["apple", "", "banana"]
print(any(s=="" for s in strings))

import os 
file_paths = ["file1.txt", "file2.txt", "file3.txt"]
print(
    any(os.path.exists(path) for path in file_paths)
    #Output depends on the existence of the files
)

# 5) all function. Like the any function, the all function returns false even if one of them is false.

num1 = [-1,-2,0, -22]

print(all(num <0 for num in num1)) #gives true


# 9) chain function 

from itertools import chain

list1 = [1,2,3]
list2 = ["a","b","c"]
combined_add = list1+list2 # This is Immediate and memory-intensive

# combined_chain= list(chain(list1,list2))
combined_chain= chain(list1,list2) # Lazy and efficient

print(next(combined_chain)) #next function gives next value from an iterable object

#We only actually need to have one new value in memory and not the whole combination of all the different values
# Iterators reference:-  https://www.youtube.com/watch?v=u3T7hmLthUU&t=0s

#10 ) Dataclass :- decorates a class
# Speicality :- Automatically implement some methods that are common when writing a dataclass

# 7) Counter function stores the count of the iterables in a dict
# speciality:- very quickly want to get the frequency of all the different objects that exist inside of an iterable object

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(words)
print(f"Count of apple is {count["apple"]}")

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    place: str
#automatic implementation of __init__ (initilaisation) , __repr__ (representation) , __eq__ (equality)
keshav = Person(name="Keshav", age=21, place="Faridabad")
dopelganger = Person(name="Keshav", age=21, place="Faridabad")

print(keshav)
print(dopelganger== keshav)

# Dataclass reference :- https://www.youtube.com/watch?v=5mMpM8zK4pY&t=0s


# 2) collections.defaultdict 
# speciality :- has a default of the object passed in the argument

from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_count = defaultdict(int)

for word in words :
    word_count[word]+=1

print(dict(word_count))


# 6) "enumerate function" is a simple function that allows you to iterate by index as well as by value when you're looping through any iterable

names = ["keshav", "Rishabh", "Arpit", "Vikrant"]

# this makes a tuple like this :- [(0,"keshav"), (1, "Rishabh"), (2, "Arpit"), (3, "Vikrant")]

for index, value in enumerate(names, start = 1):
    print(f"{index}. {value}")




# 3) Convert the python object into some type that can be easily saved in a file (json/list)
# and when loading the data you have to parse through the data and convert it back into the python object that you want

import pickle
#Pickle helps us to save any object in a file
class Human:
    def __init__(self, name, age, place):
        self.name= name
        self.age= age
        self.place = place

    def introduction(self):
        print(f"Hello, My name is {self.name}, and I am {self.age} years old. I live in {self.place}")


data = Human("Keshav", 20, "Faridabad")

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
loaded_data.introduction()

# 8) timeit function :- tells the average running time of a code snippet 
# by default it runs 1 million times

import timeit
code1= """
a= [1,2,3,4,5]
b=[x*2 for x in a]
"""
def code2():
    a=[1,2,3,4,5]
    b=list(map(lambda x:x*2 , a))

time1= timeit.timeit(code1,number= 10000)
time2= timeit.timeit(code2,number= 10000)
print("List Compression time: ",time1)
print(" Map function time",time2)
