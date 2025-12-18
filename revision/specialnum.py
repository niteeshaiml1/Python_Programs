def specialnum(num):
    temp=num
    prod=1
    sum=0
    total=0
    while temp>0:
        if temp>0 and temp<100:
            dig=temp%10
            prod*=dig
            sum+=dig
            temp//=10
    total=sum+prod
    if total==num:
        return True
    else:
        return False
num=int(input("Enter a number: "))
print(specialnum(num))