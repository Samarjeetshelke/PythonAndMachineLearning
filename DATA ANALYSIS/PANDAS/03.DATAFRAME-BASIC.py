import pandas as pd
import numpy as np

'''
data = pd.Series([1,2,3,5])
print(data)



series = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
print(series)

print(series.iloc[0])


arr = [1,2,3,4,5,6]
k=3

arr[:k],arr[k:] = arr[-k:],arr[:-k]
print(arr)'''



d = pd.DataFrame()
print(d)

print("\n")
#Empty with specified headers

d = pd.DataFrame(columns=["Name","Age","Marks"])
print(d)


#Dirctory
data = {
        "Name" : ["Samarjeet","Shree","Anii"],
        "Age":[19,20,21],
        "Subject":["English","Sanskrit","Hindi"],
        "Marks":[90,98,87]
        
        }

d = pd.DataFrame(data)
print(d)


print("\n")
#array

data = [
        
        ["Samarjeet",21,89],
        ["Shree",22,90],
        ["Anii",20,100]
    ]

d = pd.DataFrame(data,columns=["Name","Age","Marks"])
print(d)


print("\n")
#numpy
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
d = pd.DataFrame(data,index=["A","B","C"],columns=["A","B","C"])
print(d)

