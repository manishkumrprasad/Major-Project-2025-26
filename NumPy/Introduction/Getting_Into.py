import numpy as np

arr_1d = np.array([10 , 20 ,30 , 40 , 50])
# Stores array in the form of single row

arr_2d= np.array([[10,20,30],
                    [1,2,3],
                    [40,50,60]])
print("2D Array : ")
print(arr_2d)

# Multi-Dimensional Arra(Matrix)
matrix = np.array([[2, 4 ,6],
                   [10 , 20 ,30]])

print("Matrix : ")
print(matrix)

# Filing Zeroes Into The Array For Future Needs
# Holds Zereos
arr_zereos =np.zeros(3)
print("Empty Array = ",arr_zereos)

# Holds One At Each Index
arr_one =np.ones((3,3))
print("Empty 2x3 Array = ",arr_one)

# Holds Any Particular Value
arr_any = np.full((3,3) , 7)
print("Matrix Holding 7:")
print(arr_any)

# Creating Sequences Of Numbers In Numpy
# Used Through arange() #takes argument start,stop,step
ar = np.arange(1,10,2)
print("Array == ",ar)

# Identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix : ")
print(identity_matrix)