def reverse_num(num):
    rev=""
    temp=num
    while(temp>0):
        dig=temp%10
        d=str(dig)
        rev+=d
        temp=temp//10
    return int(rev)
num=int(input("Enter a number: "))
print(reverse_num(num))