#Append is used to add element to the last of the array
#Original Array Is not affected 

import numpy as np

arr_1d = np.array([1,2,3,4,5,6,7,8,9])
arr_2d = np.array([[10,20,30],[40,50,60]])


new_arr_1d = np.append(arr_1d , 10) #treatign the original array as 1d
new_arr_2d = np.append(arr_2d , [70,80,90]) #treatign the original array as 1d

print("Before Appending : ")
print(arr_1d)

print("After Appending : ")
print(new_arr_1d)
