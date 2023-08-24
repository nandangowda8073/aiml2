import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-12/Desktop/nandan/auto-mpg.csv")
print(data)
a=pd.DataFrame(data)
print(a)

#statistical details of dataset
Stats=data.describe
print(Stats)

info=(data[data['cylinders']==8]['car name'])
print(info)



