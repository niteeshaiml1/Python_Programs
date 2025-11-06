import numpy as np
a = np.random.randint(-5, 5, size=10)
b=a[a>0]
print(f"original array:{a}")
print(f"positive elements in the array:{b}")