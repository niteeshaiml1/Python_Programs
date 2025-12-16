def perfectnum (num):
    sum=0
    for i in range (1,num):
        if(num%i==0):
            sum+=i
        else:
            continue
    if(sum==num and num!=0):
        return True
    else:
        return False
        
num=int(input("Enter a number: "))
print(perfectnum(num))