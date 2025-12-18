def num_count(num):
    temp=num
    ones_count=0
    zeroes_count=0
    while temp>0:
        dig=temp%10
        temp=temp//10
        if dig==1:
            ones_count+=1
        elif dig==0:
            zeroes_count+=1
    return ones_count, zeroes_count
num=int(input("Enter a number: "))
print(num_count(num))
