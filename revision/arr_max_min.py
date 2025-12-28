
from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def max_min(arr):
    
    return sorted(arr)[-1],sorted(arr)[0]
arr=array_rep(n)
print(max_min(arr))