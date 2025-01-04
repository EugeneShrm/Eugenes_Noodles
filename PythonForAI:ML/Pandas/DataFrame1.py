import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

#create a DataFrame from the generated data (data), [index], [column], DF is a banch of series
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)
print(df["W"])
print(df[["W", "X"]])

#drop column/ row
df = df.drop("Z", axis=1) #axis=1 argument indicates that we're dropping a column
print(df)
df = df.drop("A", axis=0) #axis=0 argument indicates that we're dropping a index/row
print(df)

#row = series 
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
df = df.loc["A"] #loc = local
print(df) #shows that rows are also series

#just another example
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
df = df.loc[["A", "B"], ["W", "Y"]]
print(df)

