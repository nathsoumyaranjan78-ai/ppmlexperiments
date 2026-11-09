import numpy as np

# Creating array
harvest_data = np.array([
    [50, 55, 60, 52, 58, 65, 70],      # Tomatoes
    [30, 32, 28, 35, 33, 40, 42],      # Carrots
    [100, 95, 105, 110, 98, 120, 115], # Potatoes
    [40, 38, 42, 45, 41, 50, 55]       # Onion
])

# Part 1: Array properties
print("Harvest Data:")
print(harvest_data)

print("\nShape:", harvest_data.shape)
print("Dimensions:", harvest_data.ndim)
print("Total size:", harvest_data.size)

# Restructuring
daily_data = harvest_data.T

print("\nDays as rows and crops as columns:")
print(daily_data)

# Part 2: Statistical operations

# Total yield of each crop
total_crop_yield = np.sum(harvest_data, axis=1)

print("\nTotal yield of each crop:")
print(total_crop_yield)

# Average yield for each day
daily_average = np.mean(harvest_data, axis=0)

print("\nAverage yield for each day:")
print(daily_average)

# Maximum individual yield
maximum_yield = np.max(harvest_data)

print("\nMaximum single-crop yield:", maximum_yield, "kg")

# Part 3: Broadcasting

# Fertilizer bonus
daily_bonus = np.array([0, 0, 0, 0, 5, 10, 15])

fertilized_data = harvest_data + daily_bonus

print("\nAfter fertilizer bonus:")
print(fertilized_data)

# Crop shrinkage
shrinkage = np.array([0.95, 0.98, 0.85, 0.97])

final_weight = fertilized_data * shrinkage[:, np.newaxis]

print("\nFinal transported weight:")
print(final_weight)