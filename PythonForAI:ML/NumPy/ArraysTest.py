import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])

# Creating a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Performing element-wise addition
result = array_1d + 10

# Printing the results
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("4D Array:\n", array_3d)
print("Result of addition:", result)

