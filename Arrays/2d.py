rows,cols=3,3
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("Enter element:")))
    matrix.append(row)
    print()
print("2D Array is:",matrix)