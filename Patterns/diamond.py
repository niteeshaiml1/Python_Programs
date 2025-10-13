n=9
for i in range (n):
    for j in  range (n-i-3):
        print(end="")
    
    for j in range (i+1):
        print("*",end="")
    print()
    for j in range (6,10):
        print(end="")
    print()
    for j in range (5-2*i):
        print("*",end=" ")
    print()
    
