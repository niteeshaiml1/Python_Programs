def sum_odd_dig(num):
    sum_odd=0
    temp=num
    while temp>0:
        dig=temp%10
        temp=temp//10
        if dig%2!=0:
            sum_odd+=dig
    return sum_odd
num=int(input("Enter a number: "))
print(sum_odd_dig(num))