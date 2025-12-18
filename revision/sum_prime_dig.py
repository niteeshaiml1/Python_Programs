def sum_prime_dig(num):
    sum_prime=0
    temp=num
    while temp>0:
        dig=temp%10
        temp=temp//10
        if dig<2:
            continue
        for i in range (2,dig):
            if dig%i==0:
                break
        else:
            sum_prime+=dig
    return sum_prime
num=int(input("Enter a number: "))
print(sum_prime_dig(num))