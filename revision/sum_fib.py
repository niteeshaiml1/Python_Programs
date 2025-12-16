def sum_fib (num):
    a,b=0,1
    fib=[]
    sum=0
    for i in range (num):
        fib.append(a)
        a,b=b,a+b
    for num in fib:
        sum+=num
    return sum
num=int(input("Enter the number of terms: "))
print(sum_fib(num))
