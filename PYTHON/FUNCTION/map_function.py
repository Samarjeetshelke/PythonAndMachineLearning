
l = [1,2,3,4,5]

f = list(map(lambda x:x**2,l))
print(f)



def cube(x):
    return x**3
    
    
f = list(map(cube,l))
print(f)

k = [6,7,8,9,10]

def add(x,y):
    return x+y
    

ans = list(map(add,l,k))
print(ans)

data = ["samarjeet","rakesh","Ani"]

def getas(x):
    return [ord(i) for i in x]
    
ans = list(map(getas,data))
print(ans)
