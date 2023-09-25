import numpy as np
import random

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

# print(arr1)

data2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(data2)
# print(arr2)
# print(arr2.ndim)
# print(arr2.shape)
# print(arr2.dtype)

z = np.zeros((3, 6))
# print(z)

a1 = np.arange(15)
# print(a1)

for i in range(10):
    step = 1 if random.randint(0, 1) else -1
    print(step)
