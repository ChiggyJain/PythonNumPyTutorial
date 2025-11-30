import numpy as np

arr = np.array([10,20])
print(f"IDArr: {arr}")

print("marks of 3 students in 3 subjects")
arr = np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])
print(f"2DArr: {arr}")

print("np.arange(start, stop, step)")
arr = np.arange(1, 11)
print(f"Arrange:Arr: {arr}")

print("np.linspace(0, 1, num=5)")
arr = np.linspace(0, 1, num=5)
print(f"LinSpace: {arr}")

print("np.zeros(), np.ones(), np.full()")


print("np.zeros((3, 4))")
arr = np.zeros((3, 4))
print(f"np.zero: {arr}")

print("np.ones((3, 4))")
arr = np.ones((3, 4))
print(f"np.ones: {arr}")

print("np.full((3, 3), fill_value=5)")
arr = np.full((3,3), fill_value=5)
print(f"np.full: {arr}")


print("Random integers concept")

print("np.random.randint(1, 101, size=10)")
arr = np.random.randint(1, 101, size=10)
print(f"1DArr:np.random.int(): {arr}")

print("np.random.randint(1, 101, size=(2,3))")
arr = np.random.randint(1, 101, size=(2,3))
print(f"2DArr:np.random.int(): {arr}")


print("Random floats")
arr = np.random.random(size=5)
print(f"1DArr:np.random.random(): {arr}")

print("Normal distribution")
print("np.random.normal(loc=60, scale=5, size=10)")
arr = np.random.normal(loc=60, scale=5, size=10)
print(f"np.random.normal(loc=60, scale=5, size=10): {arr}")

print("Seed (important for testing reproducibility)")
np.random.seed(42)
arr = np.random.randint(11, 21, size=5)
print(f"Arr: {arr}")
arr = np.random.randint(11, 21, size=5)
print(f"Arr: {arr}")

print("dtype Control (Critical for interviews)")
arr = np.array([10,20], dtype=np.float32)
print(f"Arr: {arr}")
arr_int = arr.astype(np.int32)
print(arr_int.dtype)



































