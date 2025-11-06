import numpy as np
b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"mean of first column {b[:0]} is {np.mean(b[:,0])}")
print(f"mean of second column {b[:1]} is {np.mean(b[:,1])}")
print(f"mean of third column {b[:2]} is {np.mean(b[:,2])}")