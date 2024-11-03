import numpy as np

arr = np.arange(0,11)
print(arr)

arr_slice = arr[0:6]
print(arr_slice)

#Setting a value with index range (Broadcasting)
arr_slice[0:6]=100

print(arr_slice)
print(arr)
#Changes also occur in our original array! 

#if you need just copy and dont want to have relationship between entity need to use Copy
arr = np.arange(0,11)
print(arr)

arr_copy = arr.copy()
print(arr_copy)

arr_copy[0:5] = 100
print(arr_copy)
print(arr)

#but changes in original array still ocur the copy
arr[:] = 100
print(arr_copy)
print(arr)

#array indexing
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

#Indexing row v1
print(arr_2d[1,1])

#Indexing row v2
print(arr_2d[1][2])

#Index slicing
print(arr_2d[:3, 2:])

#fancy indexing
arr = np.arange(0,11)
bool_arr = arr >5
print(bool_arr)

#v1
print(arr[bool_arr])
#v2
print(arr[arr>7])

#Practice Excersice

new_arr_2d = np.arange(100).reshape(10,10)
print(new_arr_2d)

print()

# Get numbers 56, 57, 66, 67, 76, 77
print(new_arr_2d[5:8, 6:8])

