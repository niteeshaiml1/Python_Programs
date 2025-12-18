def otp_secure(num):
    temp=num
    sum_sq=0
    prod=1
    while temp>0:
        dig=temp%10
        sum_sq+=dig**2
        prod*=dig
        temp//=10
    return sum_sq-prod
num=int(input("Enter a number: "))
print("OTP Security Value:",otp_secure(num))
