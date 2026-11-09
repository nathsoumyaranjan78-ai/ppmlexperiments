import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# Statistical Operations
print("\nStatistical Operations:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# Broadcasting
print("\nBroadcasting Operations:")

# Adding a scalar to every element
print("Array + 5:")
print(arr + 5)

# Multiplying every element by a scalar
print("Array * 2:")
print(arr * 2)

# Subtracting a scalar from every element
print("Array - 10:")
print(arr - 10)