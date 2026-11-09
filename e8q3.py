import numpy as np

# Creating a NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("NumPy Array:")
print(arr)

# Array Properties
print("\nArray Properties:")
print("Number of dimensions (ndim):", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type (dtype):", arr.dtype)

# NumPy Functions
print("\nNumPy Functions:")
print("Sum of elements:", np.sum(arr))
print("Maximum element:", np.max(arr))
print("Minimum element:", np.min(arr))
print("Mean of elements:", np.mean(arr))
print("Square root of elements:")
print(np.sqrt(arr))

# Reshaping the array
print("\nReshaped Array:")
print(arr.reshape(3, 2))