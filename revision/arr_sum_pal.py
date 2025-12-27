from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def sum_pal_elements(arr):
    sum=0
    for i in range (len(arr)):
        if str(arr[i])==str(arr[i])[::-1]:
            sum+=arr[i]
    return sum
arr=array_rep(n)
print("Sum of palindrome elements is:",sum_pal_elements(arr))