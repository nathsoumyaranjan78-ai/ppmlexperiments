# Create a list containing numbers raised to their corresponding index

numbers = [2, 3, 4, 5, 6]

result = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))

print("Original list:", numbers)
print("Result:", result)