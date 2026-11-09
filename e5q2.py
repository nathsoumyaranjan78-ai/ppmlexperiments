# Function to find the key with maximum unique values

def max_unique_key(data):
    max_key = None
    max_count = 0

    for key, values in data.items():
        unique_count = len(set(values))

        if unique_count > max_count:
            max_count = unique_count
            max_key = key

    return max_key, max_count


# Create a dictionary
data = {
    "A": [1, 2, 2, 3],
    "B": [4, 4, 5],
    "C": [6, 7, 8, 8, 9]
}

key, count = max_unique_key(data)

print("Dictionary:", data)
print("Key with maximum unique values:", key)
print("Number of unique values:", count)