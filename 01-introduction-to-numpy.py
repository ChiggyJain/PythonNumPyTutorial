import numpy as np
import time
import sys

print(f"Np-Version: {np.__version__}")

arr = np.array([10,20])
print(f"Arr: {arr}")
print(f"Type: {type(arr)}")
print(f"DType of Arr-Elements: {arr.dtype}")

list1 = list(range(1_000_000))
start_time = time.time()
result = [x*x for x in list1]
end_time = time.time()
print(f"List-Processed-Via-Python and Time: {end_time-start_time}")

list1 = np.array(1_000_000)
start_time = time.time()
result = list1 * list1
end_time = time.time()
print(f"List-Processed-Via-NumPy and Time: {end_time-start_time}")

list1 = list(range(1_000_000))
print(f"List-Size-Via-Python: {sys.getsizeof(list1)}")

list1 = np.arange(1_000_000)
print(f"List-Size-Via-Np: {list1.nbytes}")

