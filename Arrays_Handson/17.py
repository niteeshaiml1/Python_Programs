import numpy as np
a = np.random.randint(-5, 5, size=10)
print(f"Original array: {a}")
for i in range (len(a)):
    if a[i]>0:
        if a[i]%2!=0:
            a[i]=a[i]*-1
print(f"Modified array with absolute values: {a}")