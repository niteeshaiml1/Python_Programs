num=int(input("enter the number:"))
temp=num
pal=0
while num>0:
    dig=num%10
    pal=pal*10+dig
    num=num//10
print(f"reverse of a number is: {pal}")    
if pal==temp:
    print("number is palindrome")
else:
    print("number is not palindrome")