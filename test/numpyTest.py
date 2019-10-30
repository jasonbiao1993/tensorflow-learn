# -*- coding: UTF-8 -*-
import numpy as np
vector = np.array([1, 2, 3])
print(vector.shape)
print(vector.size)
print(vector.ndim)
print(type(vector))


matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)
print(type(matrix))

one = np.arange(12)
print(one)
two = one.reshape((3, 4))
print(two.shape)
print(two.size)
print(two.ndim)
print(type(two))

zeros = np.zeros((3, 4))
print(zeros)
ones = np.ones((5, 6))
print(ones)
eye = np.eye(4)
print(eye)