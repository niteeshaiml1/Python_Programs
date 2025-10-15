for n in range(1, 51):
    if n <= 1:
        continue  # skip 1 and 0
    else:
        is_prime = True  # assume n is prime
        for i in range(2, n):  # check divisors from 2 to n-1
            if n % i == 0:
                is_prime = False  # found a divisor → not prime
                break
        if is_prime:
            print(n, end=", ")
