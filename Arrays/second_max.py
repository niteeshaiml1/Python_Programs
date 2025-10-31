list=[1,2,3,4,5,6,7,8,9]
max=list[0]
second_max=[]
for n in list:
    if n>max:
        second_max=max
        max=n
print("The second maximum value is:",second_max)
   
