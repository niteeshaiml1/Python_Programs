def next_prime(num):
    if num <= 1:
        return 2
    elif num == 2:
        return 3
    elif num>3:
        for i in range(2, num):
            if num % i == 0:
                num += 1
                return next_prime(num)
    return num

num=int(input("Enter a number: "))
print( next_prime(num))