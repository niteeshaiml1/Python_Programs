num=int(input("enter the number:"))
sum=0
while num > 0:
    dig=num%10
    sum+=dig
    num=num//10
print (f"Sum of digits is: {sum}")    