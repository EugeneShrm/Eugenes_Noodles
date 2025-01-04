import numpy as np

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
print(mat[3,4])
print(mat[0:3,1:2])
print(mat[4:])

#Get the sum of all the values in mat
mat = np.arange(1,26)
mat_sum = np.sum(mat)
print(mat_sum) #v1
print(mat.sum()) #v2

#Get the sum of all the columns in mat
mat = np.arange(1, 26)
# Reshape the array into a 5x5 matrix
mat_reshaped = mat.reshape(5, 5)
# Calculate the sum of each column (axis=0)
column_sums = np.sum(mat_reshaped, axis=0)
print(column_sums)

#Get the standard deviation of the values in mat
mat = np.arange(1, 26)
# Calculate the standard deviation of the values in the array
std_deviation = np.std(mat)
# Print the standard deviation
print(std_deviation)


