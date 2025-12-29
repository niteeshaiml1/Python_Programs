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
    return mat
def transpose(mat):
    transpose=[]
    for j in range (len(mat[0])):
        row=[]
        for i in range (len(mat)):
            row.append(mat[i][j])
        t=transpose.append(row)
    print("tranposed:")
    for t in transpose:
        print(*t)
    

rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
mat=matrix(rows,cols)
transpose(mat)