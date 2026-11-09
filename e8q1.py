import numpy as np

# Creating an ndarray object
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(arr)

# Indexing
print("\nIndexing:")
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])

# Slicing
print("\nSlicing:")
print("First three elements:", arr[:3])
print("Elements from index 1 to 3:", arr[1:4])
print("Last three elements:", arr[-3:])
print("Every second element:", arr[::2])