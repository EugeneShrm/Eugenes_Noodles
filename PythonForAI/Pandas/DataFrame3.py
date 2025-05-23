import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside)) #zip pair elements from multiple iterable objects
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index) #create a MultiIndex from the tuples generated by zip
print(hier_index)

#use multiple indexes
df = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
print(df)

# Assign name for index
df.index.names = ["Groups", "Num"]
print(df)

#reach needed section
print(df.loc['G1']) # Loc is used to access rows and columns in a DataFrame by their labels
print(df.loc['G1'].loc[1]["A"]) #specify 1 entity

#another way to reach specific items by xs
print(df.xs(1,level="Num"))