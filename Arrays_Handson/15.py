import numpy as np
a = np.random.randint(1, 100, size=20)
print(f"Original array: {a}")
greater_than_50 = a[a > 50]
print(f"Elements greater than 50: {greater_than_50}")
