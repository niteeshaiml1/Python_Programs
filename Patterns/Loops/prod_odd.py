a=int(input("enter start point:"))
b=int(input("enter end point:"))
prod=1
for i in range (a,b+1):
    if i%2==0:
        continue
    else:
        print(i,end=", ")
        prod*=i
print(f"\nProduct of odd numbers between {a} and {b} is: {prod}")