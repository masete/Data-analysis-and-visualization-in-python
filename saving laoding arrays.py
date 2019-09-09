import numpy as np

arr = np.arange(10)
# print arr

np.save('saved_array', arr)

#new file created and saved array

new_array = np.load('saved_array.npy')
# print new_array

#saving multiple array
array1= np.arange(30)
array2=np.arange(35)

np.savez('saved_archive.npz',x = array1,y = array2)

load_archive = np.load('saved_archive.npz')
print load_archive['x']
print load_archive['y']

#save to a text file
np.savetxt('file.txt', array1, delimiter=',')

#loading of txt files
load_txt_file = np.loadtxt('file.txt', delimiter=',')
print load_txt_file