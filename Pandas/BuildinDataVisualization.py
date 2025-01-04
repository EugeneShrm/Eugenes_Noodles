import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("df1", index_col = 0)
# print(df1.head())

df2 = pd.read_csv("df2")
# print(df2.head())

#pandas build-in data visualization 
#v1
df1["A"].hist(bins=100)#Plot a histogram of column "A" in DataFrame df1
plt.show()

#v2
df2.plot.area(alpha=0.4)# Plot an area chart of DataFrame df2 with a transparency level of 0.4
plt.show()

#v3
df2.plot.bar(stacked=True)# Plot a stacked bar chart of DataFrame df2
plt.show()

#v4
df1.plot.line(y="B")
plt.show()

