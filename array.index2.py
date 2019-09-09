import numpy as np

arr2d = np.array([[1,2,3],[4,2,5],[5,2,5]])

# print arr2d

# print arr2d[0]
# print arr2d[0][1]

#slices of 2d arrays
# slice1 = arr2d[0:2,0:3]
# print slice1

# slice2 =arr2d[:2,1:]
# print slice2[

# arr2d[:2,1:] = 15
# print arr2d

#using loopes for indexing
arr_len = arr2d.shape[0]

for i in range(arr_len):
    arr2d[i] = i;
# print arr2d

#accesing the rows

print arr2d[[0,1]]