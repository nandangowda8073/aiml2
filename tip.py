import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-12/Desktop/nandan/tips.csv")
print(data)

plt.scatter(data['day'],data['tip'])
plt.xlabel('sex')
plt.ylabel('tip')
plt.title('scatter plot')
plt.show()


plt.plot(data['tip'])
plt.plot(data['size'])
plt.bar(data['day'],data['tip'])
plt.show()

plt.hist(data['total_bill'])
plt.show()





