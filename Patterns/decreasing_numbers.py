# n=4
# for i in range(1,n+1):
#     for j in range (1,n-i):
#         print(j,end="")
#     print()
n = 4
for i in range(n, 0, -1):     # rows: 4 → 1
    for j in range(1, i + 1): # numbers: 1 → i
        print(j, end="")
    print()
