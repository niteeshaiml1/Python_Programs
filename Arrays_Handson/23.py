import numpy as np
a = np.random.randint(1,11, size=(4,4))
print(f"original matrix:{a}")
print(f"max of first row {a[0:1]} is {np.max(a[0,:])}")
print(f"max of second row {a[1:2]} is {np.max(a[1,:])}")
print(f"max of third row {a[2:3]} is {np.max(a[2,:])}")
print(f"max of fourth row {a[3:4]} is {np.max(a[3,:])}")