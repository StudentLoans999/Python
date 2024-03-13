# Example of doing vectorization (enabling operations to be performed on multiple components of a data object at the same time) by multiplying two lists together
import numpy as np

list_a = [1, 2, 3]
list_b = [2, 4, 6]

array_a = np.array(list_a)
array_b = np.array(list_b)

array_a * array_b

[2, 8, 18] # output


x = np.array([1, 2, 3, 4])
x

array([1, 2, 3, 4]) # output

x[-1] = 5
x

array([1, 2, 3, 5]) # output

arr = np.array([1, 2, 3])
arr.dtype

dtype('int64') # output

arr.shape

(3, ) # output
