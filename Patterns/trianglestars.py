n = 5
for i in range(5):                 # outer loop → rows
    for j in range(n - i):         # spaces
        print(" ", end="")
    for k in range(i + 1):         # stars
        print("*", end="")
    print()                        # move to next line
