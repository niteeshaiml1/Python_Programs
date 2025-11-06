import numpy as np

# Create a random array
a = np.array([10, 15, 20, 25, 30])
print("Original array:", a)

# Normalize to range [0, 1]
normalized = (a - a.min()) / (a.max() - a.min())
print("Normalized array:", normalized)
