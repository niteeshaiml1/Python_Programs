import numpy as np

a = np.random.randint(1, 10, size=10)
print(f"original array: {a}")


b = a[:len(a)//2]
c = a[len(a)//2:]

print(f"first half of the array: {b}")
print(f"second half of the array: {c}")
