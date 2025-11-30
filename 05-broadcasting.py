import numpy as np
import time
import sys

print("\nAdd scalar to array")
arr = np.array([1,2])
print(arr+2)

print("\nAdd 1D array to 2D rows")
m = np.array([
    [1,2,3],
    [4,5,6]
])
v = np.array([10,20,30])
print(m+v)

print("\nColumn-wise Operations: If you want to add values to each column, use shape (1, n)")
m = np.array([
    [10,20,30],
    [40,50,60]
])
col_add = np.array([[1,2,3]])
print(m+col_add)

print("\nRow-wise Operations: If you want to add to each row, use shape (m,1)")
m = np.array([
    [10,20,30],
    [40,50,60]
])
row_add = np.array([[5],[10]])
print(m+row_add)