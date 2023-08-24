import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-12/Desktop/nandan/Department_Dataset.csv")
print(data)


print(data[data['gender']=='female']['salary'].sum())

print((data[(data['gender']=='female')&(data['salary']>20000)].value_counts()))

print(data['salary'].sum())

print(data[data['gender']=='female']['Dept']=='cs')

salary=data.groupby('Dept')['salary'].sum()
      

      

