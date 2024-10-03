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





