from array import array
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def arr_ending_3(arr):
    sum=0
    for i in range (len(arr)):
        if arr[i]%10==3:
            sum+=arr[i]
    return sum
n=int(input("Length: "))
arr=array_rep(n)
print("Sum of elements ending with 3 is:",arr_ending_3(arr))