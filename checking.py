from assignment import *

n = int(input('Write a number:'))

def function(x):
    list=[]
    for i in range(x):
        list.append(result[i]['name'])
    return list
print(function(n))