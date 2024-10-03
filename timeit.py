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
