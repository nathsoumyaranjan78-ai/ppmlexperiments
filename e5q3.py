# Function to remove duplicate values from a dictionary

def remove_duplicates(data):
    result = {}

    for key, value in data.items():
        if value not in result.values():
            result[key] = value

    return result


# Input dictionary
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

# Remove duplicate values
new_dict = remove_duplicates(data)

print("Original dictionary:", data)
print("Dictionary after removing duplicates:", new_dict)