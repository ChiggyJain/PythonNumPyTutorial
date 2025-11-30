import numpy as np
import time
import sys

print("\narray.reshape(new_shape): Convert 1D → 2D")
arr = np.arange(10)
print(f"arr: {arr}")
print(f"arr: {arr.reshape(2,5)}")

print("\narray.reshape(new_shape): Convert 2D → 3D")
arr = np.arange(10)
print(f"arr: {arr}")
print(f"arr: {arr.reshape(2, 1,5)}")

print("\nreshape(-1…) Automatic Dimension")
arr = np.arange(10)
print(f"arr: {arr}")
print(f"arr: {arr.reshape(2,-1)}")

print("\nTranspose (Rows ↔ Columns)")
m = np.array([[1,2,3],[4,5,6]])
print(f"m: {m}")
print(f"m.T: {m.T}")

print("\ntranspose()")
m = np.array([[1,2,3],[4,5,6]])
print(f"m: {m}")
print(f"m.transpose(1,0): {m.transpose(1,0)}")

print("\nravel() vs flatten()")
arr = np.array([[1,2],[3,4]])
print(f"arr: {arr}")
print(f"arr.ravel(): {arr.ravel()}")
print(f"arr.flatten(): {arr.flatten()}")

print("\nsqueeze() — Remove axis with size=1")
y = np.array([[[10],[20],[30]]])
print(f"y: {y}")
print(f": {np.squeeze(y)}")

stu = np.arange(50)
stu_col = stu.reshape(-1, 5)
print(f"stud_col: {stu_col}")
