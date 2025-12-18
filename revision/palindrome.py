def palindrome(num):
    temp=num
    rev=""
    while temp>0:
        dig=temp%10
        rev+=str(dig)
        temp=temp//10
    if str(num)==rev:
        return True
    else:
        return False
num=int(input("Enter a number: "))
print(palindrome(num))