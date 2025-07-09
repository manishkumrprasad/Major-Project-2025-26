"""
!Reshaping means changing the order of the matrix 
1D -> 2D -> 3D

reshape(rows , column) -> specify the new shapes

!reshaping does not create a copy and represent a VIEW

?Remember You Can't Reshape If The Total Number Of Elements Changes
"""
import numpy as np

arr = np.array([2,4,5,6,7,8])  # 1D array with 6 elements

# 1D -> 2D      
myarr = np.array([[2,3,4],
               [5,6,7]])

reshaped_Arr = arr.reshape(2,3)
print("New Reshaped Array Matrix = " )
print(reshaped_Arr)