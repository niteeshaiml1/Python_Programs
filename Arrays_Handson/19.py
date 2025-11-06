import numpy as np

# Create a random 1D array of size 10
a = np.random.randint(1, 20, size=10)
print("Original array:", a)

# Find indices of even numbers
even_indices = np.where(a % 2 == 0)[0]
print("Indices of even numbers:", even_indices)
