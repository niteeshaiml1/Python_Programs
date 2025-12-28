from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def insert_left(arr):
    x=int(input("Enter element to insert: "))
    arr.insert(0,x)
    return arr
arr=array_rep(n)
print(insert_left(arr))    