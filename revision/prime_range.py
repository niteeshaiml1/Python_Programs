# def prime_range (start,end):
#     for i in range (start,end+1):
#         if i<=1:
#             continue
#         else:
#             for j in range (2,i):
#                 if i%j!=0:
#                     continue
#                 else:
#                     print(i)
# start=int(input("Enter the starting number: "))
# end=int(input("Enter the ending number: "))
# prime_range(start,end)
def prime_range(start, end):
    total = []   # empty list to store primes

    for i in range(start, end + 1):
        if i <= 1:
            continue

        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            total.append(i)

    return total


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

primes = prime_range(start, end)
print("Prime numbers:", primes)
print("Sum of prime numbers:", sum(primes))
