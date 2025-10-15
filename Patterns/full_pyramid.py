n = 5
for i in range(n):
    # Leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars with space
    for j in range(i + 1):
        print("*", end=" ")
    print()
