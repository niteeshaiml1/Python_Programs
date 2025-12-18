def sum_non_prime(num):
    temp=num
    non_prime=0
    while temp>0:
        dig=temp%10
        temp//=10
        if  dig==4 or dig==6 or dig==8:
            non_prime+=dig
        else:
            if dig==0 or dig==1 or dig==9 or dig==2 or dig==3 or dig==5 or dig==7:
                continue
    return non_prime
num=int(input("Enter a number: "))
print("Sum of non-prime digits:",sum_non_prime(num))