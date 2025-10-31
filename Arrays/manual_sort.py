list=[5,3,4,1,2]
for i in range (len(list)-1,0,-1):
    for j in range (i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("Sorted list is:",list)