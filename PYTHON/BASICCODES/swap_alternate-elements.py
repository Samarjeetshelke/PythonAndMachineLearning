#change the alternate elements form array

arrlist = [1,2,3,4,5,6]

i=0

while i+1<len(arrlist):
    tmp = arrlist[i]
    arrlist[i]=arrlist[i+1]
    arrlist[i+1]=tmp
    i+=2
    
print(arrlist)
