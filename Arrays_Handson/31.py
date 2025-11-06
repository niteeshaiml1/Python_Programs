import numpy as np

# Replace NaN values with mean
a=np.array([1,np.nan,3,np.nan,5])
print(a)
a[np.isnan(a)]=np.nanmean(a)
print(a)