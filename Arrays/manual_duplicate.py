list=[1,1,2,2,3,4,5,6,6]
unique=[]
for n in list:
    if n not in unique:
        unique.append(n)
print("List after removing duplicates:",unique)