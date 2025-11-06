#unable to solve remaining 

import numpy as np
# 1. Demonstrate broadcasting
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
print("Original matrix:\n",a)
print("1D array to add:",b)
c=a+b
print("After broadcasting addition:\n",c)
# 4. Simulate 1000 coin tosses
tosses=np.random.randint(0,2,1000)
heads=np.sum(tosses)
print("Number of heads in 1000 tosses:",heads)