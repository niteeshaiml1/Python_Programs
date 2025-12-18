def closest_to_21(n1, n2):
    if n1 > 21 and n2 > 21:
        return 0
    elif n1 > 21:
        return n2
    elif n2 > 21:
        return n1
    else:
        return max(n1, n2)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(closest_to_21(n1, n2))
