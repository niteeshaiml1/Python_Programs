# n=int(input("Enter length: "))
# arr=[]
# for i in range (n):
#     arr.append(0)
# print("Original array:",arr)




from itertools import repeat
z=int(input("Enter length: "))
n= list(repeat(0,z))
print("Original array:",n)