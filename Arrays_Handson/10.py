import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
v = np.vstack((a, b))
h = np.hstack((a, b))
print(f"Vertical Stack:\n{v} and horizontal Stack:\n{h}")