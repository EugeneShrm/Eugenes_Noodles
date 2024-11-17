import numpy as np
import pandas as pd
print(np.__version__)
print(pd.__version__)

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
dict = {'a':10,'b':20,'c':30}

print(labels)
print(my_data)
print(arr)
print(dict)

#Use series (one-dimensional array-like, it is similar to a list or a NumPy array, but with the ability to label each element with an index)

#v1
series = pd.Series(data = my_data) #step 1 to assign data 
print(series)

series = pd.Series(data = my_data, index = labels) #step 2 to assign index 
print(series)

#v2
series = pd.Series(arr, labels)
print(series)

#use dict
series = pd.Series(dict)
print(series)

# Use str as data (not int)
labels = ['a','b','c']
series = pd.Series(data=labels)
print(series)

#assign data/index at once
ser = pd.Series([1,2,3,4], ["USA", "Germany", "Italy", "Ukraine"])
print(ser)
print(ser["USA"])

#combine series

new_ser = ser + series
print(new_ser)

