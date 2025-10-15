# n=5
# for i in range (n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range():
#         print("*",end=" ")
#     print()   
# for i in range (n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()
n = 5

# Top half (including middle row)
for i in range(n):
    # Leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars with spaces
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Bottom half (excluding middle row)
for i in range(n - 1):
    # Leading spaces
    for j in range(i + 1):
        print(" ", end="")
    # Stars with spaces
    for j in range(n - i - 1):
        print("*", end=" ")
    print()



    