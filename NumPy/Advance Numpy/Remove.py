"""
np.delete(array , index , axis = none)
asix none means we are removing from a flatten array



"""
import numpy as np

arr = np.array([10,20,30,40,50,60])
new_arr = np.delete(arr , 0) 

print("Original Array : ")
print(arr)

print("Modified Array : ")
print(new_arr)