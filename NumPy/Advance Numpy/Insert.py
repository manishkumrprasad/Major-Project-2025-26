"""
np.insert(array , index , value , axis = none)

array -> orignal array
index -> index to which you want to insert element to
value -> value to insert at that position
asix = 0 -> row wise
       1 -> column wise

"""

import numpy as np

arr = np.array([10,20,30,40,50,60])

new_arr = np.insert(arr , 0 , 100)

# print("Original Array : ")
# print(arr)

# print("Modified Array : ")
# print(new_arr)

arr_2d = np.array([[10,20,30],[40,50,60]])

mod_arr_2d = np.insert(arr_2d , 0 , [0,0] , axis = 1) #axis 1 -> along column
mod_flatten_arr_2d = np.insert(arr_2d , 0 , [0,0] , axis = None) #axis 1 -> along column


print("Original Array : ")
print(arr_2d)

print("Modified Array :")
print(mod_arr_2d)

#when you specify the axis as none the whole array is treated as 1D
print("New Modified 2D array : ")
print(mod_flatten_arr_2d)