# Function to combine two sets and remove duplicates

def combine_sets(set1, set2):
    new_set = set1.union(set2)
    return new_set


# Input two sets
set1 = {"apple", "banana", "orange"}
set2 = {"banana", "mango", "apple"}

# Combine the sets
new_set = combine_sets(set1, set2)

print("First set:", set1)
print("Second set:", set2)
print("New set after combining:", new_set)