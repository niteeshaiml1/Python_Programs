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
def odd_even(mat):
    odd_sum=0
    even_sum=0
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            if mat[i][j]%2==0:
                even_sum+=mat[i][j]
            else:
                odd_sum+=mat[i][j]
    print(f"even sum : {even_sum} odd sum : {odd_sum}")

rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
mat=matrix(rows,cols)
odd_even(mat)