from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def arr_occ(arr):
    key=int(input("Enter element to count occurrences: "))
    count=0
    for i in range (len(arr)):
        if arr[i]==key:
            count+=1
    return count
arr=array_rep(n)
print("Occurrences of the element is:",arr_occ(arr))