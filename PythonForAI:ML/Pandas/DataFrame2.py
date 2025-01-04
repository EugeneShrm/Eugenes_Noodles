import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101) #ensuring that the random number generator results are reproducible

# Create a DataFrame 
#1
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)
print(df > 0) # Boolean DataFrame where True represents values > 0

#2 Sort rows and columns by min and plus entity
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
booldf = df > 0
print(df[booldf]) # True = numbers, Fals = null/NaN

#2.2
df_v2 = df[df["W"]>0] #show all rows in column W that are >0
print(df_v2)

#2.3
df_v3 = df[df["W"]<0] #show all rows in column W that are <0
print(df_v3)

#2.4
df_v3 = df[df["W"]<0][["X", "Y"]] #rows where column 'W' values are less than 0, showing only 'X' and 'Y' columns"
print(df_v3)

#2.5
df_v4 = df[(df["W"] < 0) & (df["X"] > 1)] #filter the DataFrame for rows where 'W' < 0 and 'X' > 1
print(df_v4)

#2.6 | = or
df_v4 = df[(df["W"] < 0) | (df["X"] > 1)] #filter the DataFrame for rows where 'W' < 0 or 'X' > 1
print(df_v4)

#3 reset/ set index

#reset
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
df = df.reset_index()
print(df)

#set
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
states = "CA NY WY OR CO" .split()
print(states)
df["States"] = states #add column to the data frame
print(df)

df = df.set_index("States") #set column as a index
print(df)