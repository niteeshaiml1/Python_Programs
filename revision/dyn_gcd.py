def gcd_dynamic():
    count = int(input("Enter number of values: "))
    numbers = []

    for i in range(count):
        n = int(input("Enter number: "))
        numbers.append(n)

    gcd = numbers[0]

    for num in numbers[1:]:
        while num != 0:
            gcd, num = num, gcd % num

    print("Input numbers:", numbers)
    print("GCD:", gcd)


gcd_dynamic()
