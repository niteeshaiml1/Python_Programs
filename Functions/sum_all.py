def sum_all(num):
    sum=0
    while num>0:
        dig=num%10
        sum+=dig
        num=num//10
    return sum
num=int(input("enter a number : "))
print(sum_all(num))
