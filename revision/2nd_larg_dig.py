def second_largest_digit(num):
    temp=num
    order=[]
    while temp>0:
        dig=temp%10
        order.append(dig)
        temp=temp//10
    order.sort()
    return order[-2]
num=int(input("Enter a number: "))
print(second_largest_digit(num))