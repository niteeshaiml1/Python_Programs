a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
if a>b:
    largest=a
    smaller=b
else:
    largest=b
    smaller=a
while largest>0:
    rem=largest%smaller
    temp=smaller%rem
print(rem)    