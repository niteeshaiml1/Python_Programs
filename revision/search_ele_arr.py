from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def search_element(arr,x):
    for i in range (len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=array_rep(n)
x=int(input("Enter element to search: "))
print("Searched element is:",search_element(arr,x))