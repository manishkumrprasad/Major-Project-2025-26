"""
!np.concat((arrayOne , arrayTwo) , axis = 0 or 1)

if axis  = 0 -> vertical stacking
           1 -> horizontal stacking
"""

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([4,5,6,7])

combined_array = np.concatenate([arr1 , arr2] , axis = 0)
print("Concenated Array : ")
print(combined_array)
