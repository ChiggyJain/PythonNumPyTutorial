import numpy as np
import time
import sys

print("Basic Indexing")
arr = np.array([10,20,30])
print(f"arr[0]: {arr[0]}")
print(f"arr[-1]: {arr[-1]}")

print("\n2D Indexing: Format → arr[row, column]")
arr = np.array([
    [11,12,13],
    [14,15,16]
])
print(f"arr[0]: {arr[0]}")
print(f"arr[0][1]: {arr[0][1]}")

print("\n1DSlicing: arr[start:end:step]")
arr = np.array([10,20,30,40,50,60])
print(f"arr: {arr}")
print(f"arr[1:4]: {arr[1:4]}")
print(f"arr[:3]: {arr[:3]}")
print(f"arr[3:]: {arr[3:]}")
print(f"arr[::2]: {arr[::2]}")

print("\n2D slicing (rows, columns)")
arr = np.array([
    [78, 85, 90], [88, 92, 76], [55, 60, 65]
])
print(f"arr: {arr}")
print(f"arr[0:2, :]: {arr[0:2, :]}")
print(f"arr[:, 1]: {arr[:, 1]}")
print(f"arr[1]: {arr[1]}")
print(f"arr[[0,1]]: {arr[[0,1]]}")

print("\nBoolean Indexing")
arr = np.array([10,20,19,30])
print(f"arr: {arr}")
print(f"arr[arr>=20]: {arr[arr>=20]}")
arr = np.arange(20)
print(f"arr: {arr}")
print(f"arr[arr%2==0]: {arr[arr%2==0]}")
arr = np.array([
    [78, 85, 90],
    [88, 92, 76],
    [55, 60, 65]
])
print(f"arr: {arr}")
print(f"arr[arr[:,1]>=85]: {arr[arr[:,1]>=85]}")

print("\n1DFancy Indexing")
arr = np.array([10, 20, 30, 40, 50])
print(f"arr: {arr}")
print(f"arr[[0,2]]: {arr[[0,2]]}")

print("\n2DFancy Indexing")
arr = np.arange(1, 17).reshape(4,4)
print(f"arr: {arr}")
print(f"arr[[0,2], :]: {arr[[0,2], :]}")
print(f"arr[:, [1,2]]: {arr[:, [1,2]]}")

print("\nSlicing returns view")
arr = np.arange(5)
print(f"arr: {arr}")
arr_slice1 = arr[0:2]
print(f"arr[0:2]: {arr_slice1}")
arr_slice1[0] = 100
print(f"arr: {arr}")

print("\nFancy indexing returns copy")
arr = np.arange(5)
print(f"arr: {arr}")
arr_slice1 = arr[[0,2]]
print(f"arr[[0,2]]: {arr_slice1}")
arr_slice1[0] = 100
print(f"arr: {arr}")

print("\nStudents who passed all subjects (>40)")
arr = np.array([
    [45, 60, 61],
    [20, 50, 55],
    [80, 70, 90]
])
print(f"arr: {arr}")
print(f"arr[np.all(arr>40, axis=1)]: {arr[np.all(arr>40, axis=1)]}")

print("\nExtract 3rd, 5th, 8th day sales")
arr = np.random.randint(100, 900, size=30)
print(f"arr[[2,4,7]]: {arr[[2,4,7]]}")



































































