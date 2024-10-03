


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
