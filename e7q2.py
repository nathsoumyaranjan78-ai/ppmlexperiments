# Add three lists using map() and lambda

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Sum of three lists:", result)