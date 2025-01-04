import numpy as np
arr = np.arange(0,11)

# + operation
arr = arr + arr
print(arr)

# * operation
arr = arr * arr
print(arr)

# + num operation
arr = arr + 111
print(arr)

# / operation
arr = arr / arr
print(arr)

#square root of each integer from 0 to 10
arr = np.arange(0,11)
print(np.sqrt(arr))

#exponential of each integer from 0 to 10
arr = np.arange(0,11)
print(np.exp(arr))

#min & max of each integer from 0 to 10
arr = np.arange(0,11)
print(np.max(arr))
print(np.min(arr))

#Sine & log of each integer from 0 to 10
arr = np.arange(0,11)
print(np.sin(arr))
print(np.log(arr))