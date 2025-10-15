# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ')
#     if i==1:
#         print(" *")
#     elif i==n:
#         print("*"+"*"*4)
#     else:
#         print("*"+' '*(i-1)+"*")        
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end='')

    if i == 1:
        print('*')
    elif i == n:
        print('*' + ' *' * (n - 1))
    else:
        print('*' + ' ' * (2*i-3) + '*')
