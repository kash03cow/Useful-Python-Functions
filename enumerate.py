
# 6) "enumerate function" is a simple function that allows you to iterate by index as well as by value when you're looping through any iterable

names = ["keshav", "Rishabh", "Arpit", "Vikrant"]

# this makes a tuple like this :- [(0,"keshav"), (1, "Rishabh"), (2, "Arpit"), (3, "Vikrant")]

for index, value in enumerate(names, start = 1):
    print(f"{index}. {value}")

