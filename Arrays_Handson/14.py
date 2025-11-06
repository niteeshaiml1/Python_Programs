# import numpy as np
# a=np.random.randint(1,10,size=10)
# print(f"original matrix:{a}")
# for n in a:
#     if n%2==0:
#         n=-1
#     print(f"modified matrix:{a}")
import numpy as np

a = np.random.randint(1, 10, size=10)
print(f"Original array: {a}")

# Replace even numbers with -1
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = -1

print(f"Modified array: {a}")
