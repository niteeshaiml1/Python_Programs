def lucky_customer(n):
    fib=[]
    a,b=1,1
    for i in range(n):
        fib.append(a)
        a,b=b,a+b
    return (fib[-1])
    print(f"Nth number is {fib[-1]}")
n=int(input("Enter the Nth number: "))
print(f"sequence is {lucky_customer(n)}")
