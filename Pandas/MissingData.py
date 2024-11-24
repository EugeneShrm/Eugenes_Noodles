import numpy as np
import pandas as pd

# NaN (Not a Number) value from numpy, which represents missing data in datasets.
d = {"A":[1,2, np.nan], "B":[5, np.nan, np.nan], "C":[1,2,3]}
print(d) #output is a row Python dictionary format

df = pd.DataFrame(d) #turn d to data frame
print(df)

# drop NaN columns/rows
print(df.dropna()) # rows & columns with no NaN value

print(df.dropna(axis=1)) # columns with no NaN value

print(df.dropna(axis=0)) # row with no NaN value

print(df.dropna(thresh=2)) #threshhold >= 2 items have value


# add missing values 
#1
df["A"] = df["A"].fillna(value=df["A"].mean()) #The mean() function calculates the average of all non-NaN values in the column "A"
print(df["A"])

#2 to assign 1 to all values in A column
df["A"] = 1  
print(df)

#3
df.loc[2, "A"] = 3
print(df)

