import numpy as np

#Create an array of 10 zeros
arr = np.zeros(10)
print(arr)

#Create an array of 10 ones
arr = np.ones(10)
print(arr)

#Create an array of 10 fives
arr = np.ones(10) * 5 # or +5
print(arr)

# Create an array of the integers from 10 to 50
arr = np.arange(10, 51)
print(arr)

#Create an array of all the even integers from 10 to 50
arr = np.arange(10, 51, 2)
print(arr)

#Create a 3x3 matrix with values ranging from 0 to 8
mat = np.array([[0,1,2], [3,4,5],[6,7,8]])
print(mat)

# v2 ^
mat = np.arange(9).reshape(3, 3)
print(mat)

#Create a 3x3 identity matrix
identity_mat = np.eye(3)
print(identity_mat)

#Generate a random numbers between 0 and 1
arr = np.random.rand(1) #generate 1 numbers between 0 and 1
print(arr)

arr = np.random.rand(2) #generate 2 numbers between 0 and 1
print(arr)

#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr = np.random.randn(25)
print(arr)

# Generates 100 random integers between 0 and 99
arr = np.random.randint(0, 100, size=10)  
print(arr)

#Create the matrix 10x10 with range 0.01
ls = np.linspace(0.01, 1,100).reshape(10,10)
print(ls)

#V2 ^
arr = np.arange(1, 101).reshape(10,10)/100
print(arr)

#Create an array of 20 linearly spaced points between 0 and 1
ls = np.linspace(0, 1, num=20, dtype=float)
print(ls)

