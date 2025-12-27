# from array import array
# def array_input(n):
#     arr=array('i',[])
#     for i in range(n):
#         ip=int(input())
#         arr.append(ip)
#     return arr
# n=int(input("Enter the number of elements: "))
# print(array_input(n))
# from array import array

# def array_input(n):
#     arr = array('i', [])
#     for i in range(n):
#         ip = int(input(f"Enter element {i+1}: "))
#         arr.append(ip)
#     return arr

# n = int(input("Enter the number of elements: "))
# print(array_input(n))
from array import array
values=list(map(int,input("Enter the elements: ").split()))
arr=array('i',values)
print(arr)