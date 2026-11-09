# Find the ratio of positive numbers, negative numbers and zeros

numbers = [2, -3, 0, 5, -1, 0, 4, -6, 7]

# Classify each number using map()
result = list(map(lambda x: "P" if x > 0 else "N" if x < 0 else "Z", numbers))

positive = result.count("P")
negative = result.count("N")
zero = result.count("Z")

print("Array:", numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Ratio (Positive : Negative : Zero):",
      positive, ":", negative, ":", zero)