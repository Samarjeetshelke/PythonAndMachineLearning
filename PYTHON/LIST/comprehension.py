# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

mylist = [1,2,3,4,5,6]

newlist = [ x** 2 for x in mylist] 
alist = [x**2 for x in mylist if x%2==0]

print(newlist)
print(alist)



mymatrix = [[1,2,3],[4,5,6],[7,8,9]]

blist = [ items** 2 for sublist in mymatrix for items in sublist]
#first we will get the subset in matrix ie sublist in mymatrix
#second we will get items in sublist ie items in sublist and then we  perform operations  on items

print(blist)

clist = [items ** 3 for sublist in mymatrix for items in sublist if items%2==0]
#it will get cubeof all number form matrix which can divide by 2 or even numbers
print(clist)
