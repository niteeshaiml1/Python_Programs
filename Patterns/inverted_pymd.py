# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(2*(n-i)-1):
#         print("*",end=" ")
#     print()    
n = 5
for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(".", end="")
    # Print stars with space
    for j in range(n - i):
        print("*", end=" ")
    print()  # Move to next line
