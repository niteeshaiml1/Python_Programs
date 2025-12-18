def odd_dif_discount(num):
    temp=num
    dis=0
    while temp>0:
        dig=temp%10
        temp//=10
        if dig%2==0:
            continue
        else:
            dis+=dig
    return dis
num=int(input("Enter a number: "))
print("Discounted amount is",odd_dif_discount(num))