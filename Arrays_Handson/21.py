import numpy as np
b = np.array([[1, 2, 3], [4, 5, 6]])
sum=0
for n in range (len(b)):
    for m in range (len(b[n])):
        sum=sum+b[n][m]
print(f"Sum of all elements in the 2D array: {sum}")