num = int(input("Enter the number: "))
a = 0
b = 1

print(a, b, end=" , ")

for i in range(2, num):
    next = a + b
    if i == num - 1:
        print(next, end=".")   # last number ends with .
    else:
        print(next, end=" , ") # others end with ,
    a = b
    b = next
