"""
vertically 
horizontally

vertical() row wise
horizontal() coulmn wise

"""


import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#prints in matrix formet
print(np.vstack((arr2 , arr1))) #Vertically Stacking


#Prints in flatten format
print(np.hstack((arr1 , arr2))) #Horizontally Stacking