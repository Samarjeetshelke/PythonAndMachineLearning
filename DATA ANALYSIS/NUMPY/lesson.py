import numpy as np

lis = [1,2,4,5,6]
lis2 = [7,8,9,10,11]

arr = np.array(lis)
arr2 = np.array(lis2)

print(lis+lis2)

res = [x+y for x,y in zip(lis,lis2)]#using explicit loop which leads to overhead

res = []

for i in range(len(lis)):
    res.append(lis[i]+lis2[i])
    
res = [lis[i]+lis2[i] for i in range(len(lis))]#explicit loopa

print(res)

print(arr+arr2)#simply using vectorized operations 
