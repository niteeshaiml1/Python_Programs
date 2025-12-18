def ijk(i,j,k):
    i_j=0
    j_k=0
    for x in range(i,j):
        i_j+=x
    print("Sum of i to j is:",i_j)
    for x in range (j,k,-1):
        j_k+=x
    print("Difference of j to k is:",j_k)
    return i_j+j_k+k
i=int(input("Enter i value: "))
j=int(input("Enter j value: "))
k=int(input("Enter k value: "))
print("Result is:",ijk(i,j,k))