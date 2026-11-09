# Function to merge two dictionaries

def merge_dict(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# Input dictionaries
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Merge the dictionaries
result = merge_dict(dict1, dict2)

print("First dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", result)