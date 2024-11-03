import numpy as np
# Generate numbers with float data type
array = np.arange(0, 100, 4.2, dtype=float)
print(array)
# Output: [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# TBD
ones_2d = np.ones((2, 3), order='C')
print("2D Array of Ones:\n", ones_2d)


# Corrected version
ls = np.linspace(0, 100, num=20, dtype=int)
print(ls)

#Create an array of 10 fives
arr = np.ones(5)*10
print(arr)

#Identity matrix
npEye = np.eye(10)
print(npEye)

#zero and one metrix
arr = np.zeros(3)
print(arr)

arr = np.ones(3)
print(arr)

arr = np.ones((3,3))
print(arr)

