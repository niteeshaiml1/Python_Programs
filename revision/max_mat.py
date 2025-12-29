def matrix(rows,cols):
    mat=[]
    for i in range (rows):
        row=[]
        for j in range(cols):
            value=int(input(f"Enter element at position ({i+1},{j+1}): "))           
            row.append(value)
        mat.append(row)
    for row in mat :
        print(*row)
    return mat
def max(mat):
    m=0
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            if mat[i][j]>m:
                m=mat[i][j]
    return m
rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
mat=matrix(rows,cols)
print("Maximum element in matrix is:",max(mat))