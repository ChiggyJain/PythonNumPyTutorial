import numpy as np
import time
import sys

print("\nElement-wise Operations")
arr = np.array([1, 2, 3, 4])
print(f"arr: {arr}")
print(f"arr+2: {arr+2}")
print(f"arr-2: {arr-2}")
print(f"arr*2: {arr*2}")
print(f"arr%2: {arr%2}")

print("\nVectorized Arithmetic: On two 1D arrays:")
a = np.array([10,20,30])
b = np.array([1,2,3])
print(a+b)
print(a-b)
print(a*b)

print("\nMatrix Arithmetic: On 2D Arrays")
m1 = np.array([
    [1,2], [3,4]]
)
m2 = np.array([
    [10,20], [30,40]]
)
print(f"m1: {m1}")
print(f"m1: {m2}")
print(f"m1+m2: {m1+m2}")
print(f"m1*m2: {m1*m2}")

print("\nComparison Operations (Vectorized): 1DArray")
arr = np.array([1, 2, 3, 4])
print(f"arr: {arr}")
print(f"arr>=3: {arr>=3}")
print(f"arr==3: {arr==3}")
print(f"arr[arr==3]: {arr[arr==3]}")

print("\nLogical Operations: students who scored 60–80")
marks = np.array([45, 62, 78, 55, 89, 70])
print(f"marks: {marks}")
print(f"marks[(marks>=60) & (marks<=80)]: {marks[(marks>=60) & (marks<=80)]}")


print("\nAggregations — Fastest Calculations: 1DArray")
arr = np.array([10,20,30,40,50])
print(f"arr: {arr}")
print(f"arr.sum(): {arr.sum()}")
print(f"arr.max(): {arr.max()}")
print(f"arr.min(): {arr.min()}")
print(f"arr.std(): {arr.std()}")
print(f"arr.var(): {arr.var()}")

print("\nAggregation with axis (Critical): 2DArray")
arr = np.array([
    [78, 85, 90],
    [88, 92, 76],
    [55, 60, 65]
])
print(f"arr: {arr}")
print(f"arr.sum(axis=1):RowLvl: {arr.sum(axis=1)}")
print(f"arr.sum(axis=0):ColLvl: {arr.sum(axis=0)}")


















