def replace_negatives(a):
    for i in range (len(a)):
        if a[i]<0:
            a[i]=0
    return a
a=[1,2,3,-1,-2,-3,-4]
print(replace_negatives(a))