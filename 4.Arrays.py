import numpy as np

myArray = [1,2,3,4]

type(myArray)

# not supported as it is a list
print(myArray ** 2 )

arr1 = np.array(myArray)
print(arr1 * 2)
print(arr1 ** 2)
print(arr1 ** 2 + arr1)

print(arr1 > 2)
print(arr1[arr1 > 2])

arr1.max()
arr1.mean()
arr1.min()

# Matrix based operations

matrix1 = np.array([[1,2],[3,4],[3,5]])
print (matrix1 * 1)

# Item wise addition
print (matrix1 + 1)

# Element wise multiplication
print (matrix1 * 10)
matrix2 = np.array([
        [1,2,3],
        [3,4,5]
        ])
print (matrix1 * matrix2)

# Matrix Multiplication
matrix1.dot(matrix2)

# Reshape the array
matrix2.reshape((2,3))

# statistics from matrix

matrix2.max(axis=0)

matrix2.min(axis=0)
