import numpy as np
import matplotlib.pyplot as plt

axes_values = np.arange(-100,100,10)

dx, dy = np.meshgrid(axes_values,axes_values)

# print 'dx'
# print dx

# print 'dy'
# print dy

function = 2*dx + 3*dy
function1 = np.cos(dx)+ np.cos(dy)
print function


# plt.imshow(function)
plt.imshow(function1)
# plt.title('function of plot of 2*dx + 3*dy')
plt.title('function to plot np.cos(dx)+ np.cos(dy)')
plt.colorbar()
# plt.savefig('myfig.png')
plt.savefig('myfig1')