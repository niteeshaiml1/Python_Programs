def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    return fact

num = int(input("Enter a number to find its factorial: "))
print(factorial(num))
