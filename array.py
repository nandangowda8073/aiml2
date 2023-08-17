import numpy as np
a=np.array([[1,2,3],[3,4,5]])
b=np.array([[9,5,3],[3,1,5]])
print(a.ndim)
print(a.sum())
print(a.sum(axis=1))
print(a.max())
print(a.min())
print(a.max(axis=1))
print(b.min(axis=1))
print(a.transpose())
print("sum of two matrix",a+b)
print("sub of two matrix",a-b)

