import time
import numpy as np

# Create large lists and arrays for comparison
size = 1000000
list1 = list(range(size))
list2 = list(range(size))
array1 = np.array(list1)
array2 = np.array(list2)

# Time the Python list operation
start_time = time.time()
result_list = [list1[i] + list2[i] for i in range(size)]
end_time = time.time()
print("Python list time:", end_time - start_time)

# Time the NumPy array operation
start_time = time.time()
result_array = array1 + array2
end_time = time.time()
print("NumPy array time:", end_time - start_time)
