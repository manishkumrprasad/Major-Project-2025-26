import numpy as np


arr = np.array([[10,20,30] , [40,50,60] , [70,80,90]])
new_arr = np.delete(arr , 0 , axis = 0)

print("Original Array :")
print(arr)


print("Modified Array : ")
print(new_arr)