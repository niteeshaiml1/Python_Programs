def merge(a,b):
    merged=[]
    for i in a:
        merged.append(i)
    for j in b:
        merged.append(j)
    return merged
    print(merged)
a=[1,2,3]
b=[4,5,6]
merge(a,b)