
#passsing single arguments
def printf(a):
    print(a)
    
printf(34)

#passing multiple arguments
def add(a,b):
    print(a+b)

add(12,90)

#passing single list or arguments
def func(data):
    for i in data:
        print(i)


d = [2,3,4,5,6]
func(d)

#passing multiple list [Variable-Length Arguments]
#when the number of arguments is not clear
def func(*data):
    for i in data:
        for j in i:
            print(j)


d = [2,3,4,5,6]
e =[7,8,9,10]
func(d,e)


#docstring
def multiply(a, b):
    """This function multiplies two numbers and returns the result."""#this is doc string
    return a * b

print(multiply.__doc__)  # Output: This function multiplies two numbers and returns the result.


