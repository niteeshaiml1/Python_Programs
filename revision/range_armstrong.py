def range_armstrong(start,end):
    for num in range(start,end+1):
        temp=num
        count=len(str(num))
        sum=0
        while temp>0:
            dig=temp%10
            sum=sum+(dig**count)
            temp=temp//10
        if sum==num:
            print(f"{num} is an Armstrong number")
        
start=int(input("Enter the starting number of the range: "))
end=int(input("Enter the ending number of the range: "))
range_armstrong(start,end)