def niven_num(num):
    temp=num
    sum=0
    while temp>0:
        dig=temp%10
        sum+=dig
        temp//=10
    if num%sum==0:
        return True
    else:
        return False
        
num=int(input("Enter a number: "))
print(niven_num(num))