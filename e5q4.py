# Function to copy a set

def copy_set(original):
    new_set = set()

    for element in original:
        new_set.add(element)

    return new_set


# Input set
original = {10, 20, 30, 40, 50}

# Copy the set
new_set = copy_set(original)

print("Original set:", original)
print("New set:", new_set)