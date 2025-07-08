"""
!Flattering is used for reshaping multi-dimensinal array to 1D array

ravel affects the original array and it return the view
while flatter does not affect the original array and it returns the copy of the original array


"""

import numpy as np

arr_2d = np.array([[2,3,4],[4,5,6]])
print("Matrix : ")
print(arr_2d)

flatten_2d = arr_2d.flatten()

print("Flatten Array = " , flatten_2d)