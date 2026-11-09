import numpy as np

# Creating NumPy arrays with different data types

# Integer data type
a = np.array([10, 20, 30, 40], dtype=int)

# Float data type
b = np.array([10.5, 20.5, 30.5], dtype=float)

# String data type
c = np.array(["Apple", "Banana", "Mango"], dtype=str)

# Boolean data type
d = np.array([True, False, True], dtype=bool)

# Displaying arrays and their data types
print("Integer Array:", a)
print("Data Type:", a.dtype)

print("\nFloat Array:", b)
print("Data Type:", b.dtype)

print("\nString Array:", c)
print("Data Type:", c.dtype)

print("\nBoolean Array:", d)
print("Data Type:", d.dtype)

# Different data structures in NumPy

# 1-D array
one_d = np.array([1, 2, 3, 4])

# 2-D array
two_d = np.array([[1, 2], [3, 4]])

# 3-D array
three_d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])

print("\n1-D Array:")
print(one_d)

print("\n2-D Array:")
print(two_d)

print("\n3-D Array:")
print(three_d)