from array import array
import math
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter{i+1}th value:"))
        arr.append(value)
    return arr
def strong_num(arr):
    sum=0
    for num in arr:
        temp=num
        count=0
        while temp>0:
            dig=temp%10
            count+=math.factorial(dig)
            temp//=10
        if count==num:
            sum+=num
    return sum  
n=int(input("Length: "))
arr=array_rep(n)
print("Sum of strong numbers is:",strong_num(arr))