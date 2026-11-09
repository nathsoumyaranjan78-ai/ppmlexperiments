# Convert list and tuple of integers into strings using map()

list1 = [10, 20, 30, 40]
tuple1 = (50, 60, 70, 80)

list_result = list(map(str, list1))
tuple_result = list(map(str, tuple1))

print("Original list:", list1)
print("List of strings:", list_result)

print("Original tuple:", tuple1)
print("List of strings:", tuple_result)