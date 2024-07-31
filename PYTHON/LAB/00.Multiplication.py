
import numpy as np

mat1 = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    
mat2 = np.array([
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ])
    
ans = np.zeros((3,3))

#Addition
for i in range (0,3):
    for j in range(0,3):
        ans[i][j] = mat1[i][j]+mat2[i][j]
    


# for i in range (0,3):
#     for j in range(0,3):
#         print(ans[i][j])
        
#     print
print("Addition: ")
print(ans)

for i in range (0,3):
    for j in range(0,3):
        ans[i][j] = mat1[i][j]-mat2[i][j]


print("Substraction: ")
print(ans)

  

anss = np.zeros((3,3))



for i in range(0,3):
    for j in range(0,3):
        for k in range (0,3):
           anss[i][j] += mat1[i][k] * mat2[k][j]
        
            
         
            
print("Multiplication: ")
print(anss)

