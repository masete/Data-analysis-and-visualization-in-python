import numpy as np
arr = np.arange(0, 12)

# print arr
print arr[0:5]
print arr[2:8]

# arr[0:5] = 20

arr2 = arr[0:6]

arr2[:] =29

print arr2

#creating new array copy
arrcopy = arr.copy()

print arrcopy