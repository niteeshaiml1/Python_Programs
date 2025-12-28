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
rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
# Sum of matrix elements
# def sum_matrix(mat):
#     sum=0
#     for row in mat:
#         for value in row:
#             sum+=value
#     return sum
# mat=matrix(rows,cols)
# print("Sum of matrix elements is:",sum_matrix(mat))

# sum of even elements of matrix
# def sum_even(mat):
#     sum=0
#     for row in mat:
#         for value in row:
#             if value%2==0:
#                 sum+=value
#     return sum
# mat=matrix(rows,cols)
# print("Sum of even elements is:",sum_even(mat))


#prime elements sum in matrix
# def sum_prime(mat):
#     sum=0
#     for row in mat:
#         for value in row:
#             if value>1:
#                 is_prime=True
#                 for j in range(2,int(value**0.5)+1):
#                     if value%j==0:
#                         is_prime=False
#                 if is_prime:
#                     sum+=value
#     return sum
# mat=matrix(rows,cols)
# print("Sum of prime elements is:",sum_prime(mat))



# sum diagonal elements
def prod_diagonal(mat):
    sum=1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i==j:
                sum*=mat[i][j]
    return sum
mat=matrix(rows,cols)
print("Product of diagonal elements is:",prod_diagonal(mat))


# mat=matrix(rows,cols)
# print(sum_diagonal(mat))




#sum of first and last element

# def sum_first_last(mat):
#     return mat[0][0]+mat[-1][-1]
# mat=matrix(rows,cols)
# print("Sum of first and last element is:",sum_first_last(mat))