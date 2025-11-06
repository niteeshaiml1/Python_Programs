a=[1,2,3,4,5]
b=[3,4,5,6,7]
common=[]
for n in a:
    if n in b:
        common.append(n)
print("Common elements are:",common)
