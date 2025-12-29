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
def identity(mat):
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            if i == j:
                if mat[i][j] != 1:
                    return False
            else:
                if mat[i][j] != 0:
                    return False

    return True
rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
mat=matrix(rows,cols)
print(identity(mat))