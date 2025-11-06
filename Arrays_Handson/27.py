import numpy as np
a=np.random.randint(1,11,size=(3,3))
print(f"original matrix:{a}")
print(f"mean of first column {a[:,0]} is {np.mean(a[:,0])}")
print(f"mean of second column {a[:,1]} is {np.mean(a[:,1])}")
print(f"mean of third column {a[:,2]} is {np.mean(a[:,2])}")
for i in range(len(a)):
    a[i,0]=a[i,0]-np.mean(a[:,0])
    a[i,1]=a[i,1]-np.mean(a[:,1])
    a[i,2]=a[i,2]-np.mean(a[:,2])
print(f"matrix after subtracting mean of each column:{a}")
