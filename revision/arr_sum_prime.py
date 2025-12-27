from array import array 
n=int(input("Length: "))
def array_rep(n):
    arr=array('i',[])
    for i in range (n):
        value=int(input(f"enter {i+1}th element:"))
        arr.append(value)
    return arr
def sum_prime_elements(arr):
    sum=0
    
    for i in range (len(arr)):
        if arr[i]>1:
            is_prime=True
            for j in range(2,int(arr[i]**0.5)+1):
                if arr[i]%j==0:
                    is_prime=False
                
            if is_prime:
                sum+=arr[i] 
    return sum
arr=array_rep(n)
print("Sum of prime elements is:",sum_prime_elements(arr))