n=4
for i in range (n):
    for j in range (n-i-1):
        print(end=" ")
    for i in range (i+1):
        print("*",end=" ")
    print() 