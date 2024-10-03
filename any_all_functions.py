
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
