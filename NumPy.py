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


arr.shape # used to check the shape of an array

(3, ) # output


arr.ndim # used to check the number of dimensions of an array

1 # output

# An array of two lists
arr_2d = np.array([[1, 2], 
                   [3, 4], 
                   [5, 6], 
                   [7, 8]])
print(arr_2d.shape)
print(arr_2d.ndim)
arr_2d

# Output
(4, 2) # 4 rows, 2 columns
2 # 2 dimensions
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])

# An array of three lists
arr_3d = np.array([[[1, 2, 3],
                    [3, 4, 5]],
                   
                   [[5, 6, 7],
                    [7, 8, 9]]]
)
print(arr_3d.shape)
print(arr_3d.ndim)
arr_3d

# Output
(2, 2, 3)
3 # 3 dimensions
array([[[1, 2, 3],
        [3, 4, 5]],
       
       [[5, 6, 7],
        [7, 8, 9]]])


arr_2d = arr_2d.reshape(2, 4) # .reshape() - used to change the shape of an array (use the arr_2d from above)

array([[1, 2, 3, 4],
       [5, 6, 7, 8]])


arr = np.array([1, 2, 3, 4, 5])
np.mean(arr) # gets the mean
np.log(arr) # gets the log

3.0 # output
array([0. , 0.69314718, 1.09861229, 1.38629436, 1.60943791])


np.floor(5.7) # rounds down
np.ceil(5.3) # rounds up

5.0 # output
6.0

np.zeros((3, 2)) # creates array of designated shape pre-filled with 0s

[[ 0. 0.]
 [ 0. 0.]
 [ 0. 0.]]

np.ones((2, 2)) # creates array of designated shape pre-filled with 1s

[[ 1. 1.]
 [ 1. 1.]]

np.full((5, 3), 8) # creates array of designated shape pre-filled with a specified value

[[ 8. 8. 8. ]
 [ 8. 8. 8. ]
 [ 8. 8. 8. ]
 [ 8. 8. 8. ]
 [ 8. 8. 8. ]]


array_2d = np.array([(1, 2, 3), (4, 5, 6)])
print(array_2d)
print()
array_2d.flatten() # .flatten() - returns a copy of the array collapsed into one dimension
print()
array_2d.reshape(3, 2) # .reshape() - gives a new shape to an array without changing its data
print()
array_2d.reshape(3, -1) # adding a value of -1 in the designated new shape makes the process more efficient, as it indicates for NumPy to automatically infer the value based on other given values
print()
array_2d.tolist() # .tolist() - converts an array to a list object. Multidimensional arrays are converted to nested lists 

[[1 2 3] # output
 [4 5 6]]

[1 2 3 4 5 6] # here it was flattened

[[1 2] # here it was reshaped
 [3 4]
 [5 6]]

[[1 2] # second time it was reshaped
 [3 4]
 [5 6]]

[[1, 2, 3], [4, 5, 6]] # here it was conveted to 2 lists

## Mathematical functions
print(array_2d.max())
print(array_2d.min())
print(array_2d.mean())
print(array_2d.std())


array_2d = np.array([(1, 2, 3), (4, 5, 6)])
print(array_2d)
print()
print(array_2d.size) # returns the total number of elements in the array
print(array_2d.T) # returns the array transposed (rows become columns, columns become rows)

[[1 2 3] # output
 [4 5 6]]

6 # here size is given
[[1 4] # here it was transposed
 [2 5]
 [3 6]]

## Indexing and Slicing
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
print()

print(a[1])
print(a[0, 1])
print(a[1, 2])
print()
a[:, 1:]

[[1 2 3] # output
 [4 5 6]]

[4 5 6]
2 
6

[[2 3] # select all rows (: before the comma) and all columns starting from the second column onwards (1: after the comma)
 [5 6]]

## Math operations
a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([[1, 2, 3], [1, 2, 3]])

print(a + b)
print()
print(a * b)

[[2 4 6] # output
 [5 7 9]]

[[ 1  4  9]
 [ 4 10 18]]


a = np.array([(1, 2), (3, 4)]) # arrays are mutable but with certain limitations; an existing element can be changed
a[1][1] = 100
a

[[  1   2] # output
 [  3 100]]

a[3] = 100 # but an array can't be lengthened or shortened so this will result in an error
a
