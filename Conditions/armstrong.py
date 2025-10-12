num=int(input("Enter a number: "))
temp=num
arm=0
while num>0:
    t=num%10
    arm+=t**3
    num=num//10
print(arm)    
if arm==temp:
    print("number is armstrong")    
else:
    print("number is not armstrong")
