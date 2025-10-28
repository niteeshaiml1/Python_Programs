a=[[1,2],[3,4],[2,3]]
sum=0
for i in range (len(a)):
    for j in range (len(a[i])):
        print(a[i][j],end=" ")
        sum+=a[i][j]
    print()
print("Sum:",sum)
