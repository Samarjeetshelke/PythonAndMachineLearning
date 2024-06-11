
#find the Duplicate elemet form list

alist = [1,2,3,4,3] # range 1-4 pr 1 - (size-1)
i=0

for x in alist:#thisi loop will add all the number form 1 to 4 but dilete the  duplicates
    i = i^ x

for x in range(1,5):#it will remove all the number form i but not able to remove the duplicate coz its already been removed form array
    i = i^ x
    
print(i)
