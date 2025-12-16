def harshadnum (num):
    temp=num
    div=0
    while(temp>0):
        dig=temp%10
        div+=dig
        temp=temp//10
    print(div)
    if(num%div==0):
        return True 
    else:
        return False
num=int(input("Enter a number: "))
print(harshadnum(num))