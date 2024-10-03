# 7) Counter function stores the count of the iterables in a dict
# speciality:- very quickly want to get the frequency of all the different objects that exist inside of an iterable object

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(words)
print(f"Count of apple is {count["apple"]}")

