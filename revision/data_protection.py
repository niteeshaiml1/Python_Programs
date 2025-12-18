def data(num):
    temp=num
    rev=""
    while temp>0:
        dig=temp%10
        rev+=str(dig)
        temp//=10
    return int(rev)+num
num=int(input("Enter a number: "))
print("Result after adding reverse:",data(num))