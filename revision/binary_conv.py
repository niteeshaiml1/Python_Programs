def conversion(num):
    binary=""
    while num>0:
        rem=num%2
        binary=str(rem)+binary
        num=num//2
    return binary
num=int(input("Enter a decimal number: "))
print(conversion(num))