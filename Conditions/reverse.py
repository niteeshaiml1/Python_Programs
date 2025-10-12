num=int(input("enter a number: "))
rev=0
while num>0:
    i=num%10
    rev=rev*10+i
    num=num//10
print(f"reverse of the number is {rev}")
   