def intersection(arr1, arr2):
    return list(filter(lambda x: x in arr2, arr1))


arr1 = list(map(int, input("Enter elements of first array: ").split()))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

result = intersection(arr1, arr2)

print("Intersection of the two arrays:", result)