def armstrong (num):
    count=len(str(num))
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        sum=sum+(dig**count)
        temp=temp//10
    if sum==num:
        return True
    else:
      return False
num = int(input("Enter a number to check if it is an Armstrong number: "))
print(armstrong(num))