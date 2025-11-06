import numpy as np
a=np.array([1,2,2,3,3,3,3])
u,c=np.unique(a,return_counts=True)
print(u)
print(c)