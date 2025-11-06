list=[1,2,3,4,5,6,7,8,9]
even=odd=zero=0
for n in list:
    if n%2==0:
        even+=1
    elif n==0:
        zero+=1
    else:
        odd+=1
print("Even numbers count is:",even)
print("Odd numbers count is:",odd)
print("Zero count is:",zero)