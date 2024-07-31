lis = [2,5,34,987,7,4];
small = lis[0]
lag = lis[0]

for i in lis:
    if i<small:
        small = i
        
    if i>lag:
        lag = i
        

print(f"Min: {small} Max: {lag}");
