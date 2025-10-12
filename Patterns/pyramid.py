n = 5  # number of rows

for i in range(1, n+1):            # Outer loop → controls rows
    for j in range(n - i):          # First inner loop → print spaces
        print(" ", end="")
    for k in range(2 * i - 1):      # Second inner loop → print stars
        print("*", end="")
    print()                         # Move to next line after each row
