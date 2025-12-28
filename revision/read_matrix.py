def matrix(rows,cols):
    mat=[]
    for i in range (rows):
        row=[]
        for j in range (cols):
            value=int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(value)
        mat.append(row)
    for row in mat :
        print(*row)
rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
print(matrix(rows,cols))