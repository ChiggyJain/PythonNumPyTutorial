import numpy as np
import time
import sys

print("\nargmax & argmin: These return index, not the value.")
arr = np.array([10, 30, 20, 40, 5])
print(f"arr: {arr}")
print(f"arr.argax(): {arr.argmax()}")
print(f"arr.argmin(): {arr.argmin()}")

print("\n2D argmax (Important!): Find student index with highest total marks:")
arr = np.array([
    [78, 85, 90],
    [88, 92, 76],
    [55, 60, 65]
])
print(f"arr: {arr}")
print(f"Each-Student-Total-Marks: { (arr.sum(axis=1)) }")
print(f"Highest-Total-Marks-Student-Indx: { (arr.sum(axis=1)).argmax() }")

print("\nCumulative Operations")
arr = np.array([10, 20, 30])
print(f"arr: {arr}")
print(f"arr.cumsum(): {arr.cumsum()}")
print(f"arr.cumprod(): {arr.cumprod()}")

print("\nPercentiles")
arr = np.array([50, 60, 70, 80, 90])
print(f"arr: {arr}")
print(f"np.percentile(arr, 60): {np.percentile(arr, 60)}")

print("\nSort values")
arr = np.array([50, 60, 70, 63, 90])
print(f"arr: {arr}")
print(f"np.sort(arr): {np.sort(arr)}")
print(f"arr.argsort(): {arr.argsort()}")

