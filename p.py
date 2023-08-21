import pandas as pd
import numpy as np
info=np.array([10,20,30])
a=pd.Series(info)
print(a)

p=pd.Index([1,2,3,np.nan,5])
print(p.value_counts())


p=pd.Index([1,2,3,np.nan,5])
print(p.value_counts())


