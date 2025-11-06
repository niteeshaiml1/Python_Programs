import numpy as np
a=np.array([1,2,3,4,5])
print(np.std(a))
print(np.var(a))

def euclidean_distance(x,y):
    return np.sqrt(np.sum((x-y)**2))
v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(euclidean_distance(v1,v2))

v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(np.dot(v1,v2))
print(np.cross(v1,v2))
