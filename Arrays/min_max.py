list=[1,2,3,4,5,6,7,8,9]
min=max=list[0]
for n in list:
    if n<min:
        min=n
    if n>max:
        max=n
print("Minimum value is:",min)
print("Maximum value is:",max)