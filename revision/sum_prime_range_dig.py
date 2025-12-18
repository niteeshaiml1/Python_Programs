def sum_prime_range(start, end):
    total = 0

    for num in range(start, end + 1):
        if num < 2:
            continue

        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            total += num

    return total


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(sum_prime_range(start, end))
