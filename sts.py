import pandas as  pd
import numpy as np
data={'days':[1,2,3,4,5,6,7,8,9,10],'steps':[4335,9552,7332,4504,5335,7552,8352,6504,8965,1689]}
print(data)
df=pd.DataFrame(data)
print(df)

df['steps']=df['steps']+1000
print(df)

d=pd.DataFrame(data)
print(d.loc[d['steps']>7000])


