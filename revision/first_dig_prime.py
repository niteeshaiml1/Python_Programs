def first_dig_prime(num):
    temp=num
    ip=0
    while temp>0:
        dig=temp%10
        temp//=10
    ip=dig
    for i in range (2,ip):
        if ip%i==0:
            return False
    return True
num=int(input("Enter a number: "))
print(first_dig_prime(num))