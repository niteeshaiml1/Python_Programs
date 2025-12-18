def sum_prime_factors(num):
    total = 0

    for i in range(2, num + 1):
        if num % i == 0:
            # check if i is prime
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                total += i

    return total

num = int(input("Enter a number: "))
print(sum_prime_factors(num))
