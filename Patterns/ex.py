num=int(input("Enter a number: "))
for i in range (num):
    for j in range(num-i):
        print("*",end=" ")
    print()