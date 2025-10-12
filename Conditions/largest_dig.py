num = int(input("Enter a number: "))
largest = 0

while num > 0:
    flag_1 = num % 10
    if flag_1 > largest:
        largest = flag_1
    num = num // 10

print(f"Largest digit is: {largest}")
