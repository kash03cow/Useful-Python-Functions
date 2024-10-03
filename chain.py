
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
