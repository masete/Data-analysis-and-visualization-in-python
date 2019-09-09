import numpy as np

my_list1 = [1,2,3,4]
my_list2 = [5,7,3,2]

my_array = np.array([my_list1,my_list2])
# print my_array

#usage of shape functions
# print my_array.shape

#finding out the datatype of the contents of the array
# print my_array.dtype

#ones empty zeros arrange eye
# new_array = np.zeros(5) #creates new numpy array with (1*5) all elements are zeros

# new_array = np.ones([5,5]) #two dimentional array of ones
# new_array = np.empty(5)
# new_array = np.eye(5)

new_array = np.arange(5,50,3)
print new_array




