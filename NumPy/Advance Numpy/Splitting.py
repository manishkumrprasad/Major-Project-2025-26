"""
np.split() -> splits in equalt halves

np.hsplit()
np.vsplit()

"""

import numpy as np

arrOne = np.array([10,20,30,40,50,60])
arrTwo = np.array([10,20,30,40,50,60,70])


print(np.split(arrOne , 3))

print(np.hsplit(arrOne , 2))
