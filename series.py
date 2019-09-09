import pandas as pd
from pandas import Series
import numpy as np

object = Series([10,15,20,25])
# print object

# print object.values
# print object.index

data_array = np.array(['a','b','c'])  #numpy arrays
s = Series(data_array)
print s

#custom index's
s = Series(data_array, index=[])