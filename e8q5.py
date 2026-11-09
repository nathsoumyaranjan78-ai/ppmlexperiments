import numpy as np

# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# Saving the array to a file
np.save("my_array.npy", arr)
print("\nArray saved successfully.")

# Loading the array from the file
loaded_arr = np.load("my_array.npy")

print("\nLoaded Array:")
print(loaded_arr)