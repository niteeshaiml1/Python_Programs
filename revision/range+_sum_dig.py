def range_sum_dif(start,end):
    sum=0
    for i in range (start,end+1):
        temp=i
        while temp>0:
            dig=temp%10
            sum+=dig
            temp//=10
    return sum  

start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
print(range_sum_dif(start,end))