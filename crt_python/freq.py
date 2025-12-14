a=[1,2,3,4,4,5,5,5,6,7,8,8,9]
freq=0
b=int(input("enter a number to check"))
for i in range (len(a)):
    
    if a[i]==b:
        freq=freq+1
print("frequency of",b,"is",freq)