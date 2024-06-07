tu = ("samarjeet","ram","sham","sita","rakesh");
print(tu)


for item in tu :
    print(item+"\n")
    

print("\nTuple Unpacking")

#one,two,three = tu
#this cause error coz number should same as element
#print(one,two,three)


one,two,three,four,five = tu
print(one,two,three,four,five+"\n")

print("Unpacking with fewer elements")

none,_,_,_,nfive = tu
print(none,nfive+"\n")


print("Using * sign")

uno,dos,*tres = tu
print(f"{uno},{dos},{tres}\n")


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
