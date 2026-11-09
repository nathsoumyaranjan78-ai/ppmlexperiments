# Function to perform set operations

def set_operations(set1, set2):
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (Set1 - Set2):", set1 - set2)
    print("Difference (Set2 - Set1):", set2 - set1)
    print("Symmetric Difference:", set1 ^ set2)
    print("Set1 is subset of Set2:", set1 <= set2)
    print("Set2 is subset of Set1:", set2 <= set1)
    print("Set1 is superset of Set2:", set1 >= set2)
    print("Set2 is superset of Set1:", set2 >= set1)


# Input two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

set_operations(set1, set2)