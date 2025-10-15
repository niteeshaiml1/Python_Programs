# for i in range(1,5):
#     for j in range (i):
#         print("*\n ",end="")
#     print()
for i in range(1, 5):       # for each row
    for j in range(i):       # print 'i' stars in each row
        print("*", end=" ")  # stars separated by space
    print()                  # newline after each row
