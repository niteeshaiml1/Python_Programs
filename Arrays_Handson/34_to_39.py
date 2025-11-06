import numpy as np

# Merge two arrays and remove duplicates
a=np.array([1,2,3])
b=np.array([3,4,5])
c=np.unique(np.concatenate((a,b)))
print(c)

# Random 10x10 matrix and min,max,mean
a=np.random.rand(10,10)
print(a.min(),a.max(),a.mean())

# Correlation coefficient between two arrays
a=np.array([1,2,3,4,5])
b=np.array([5,4,3,2,1])
print(np.corrcoef(a,b))

# Random 5x5 matrix and threshold 0.5
a=np.random.rand(5,5)
a[a>0.5]=1
a[a<=0.5]=0
print(a)

# Eigenvalues and eigenvectors of symmetric 3x3 matrix
a=np.array([[2,1,1],[1,2,1],[1,1,2]])
w,v=np.linalg.eig(a)
print(w)
print(v)

# Save and load a NumPy array
a=np.array([1,2,3,4,5])
np.save('array.npy',a)
b=np.load('array.npy')
print(b)