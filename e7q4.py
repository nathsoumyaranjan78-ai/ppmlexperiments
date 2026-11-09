# Convert characters to uppercase and lowercase
# and eliminate duplicate letters

sequence = "Programming"

# Eliminate duplicate characters while preserving order
unique = list(dict.fromkeys(sequence))

uppercase = list(map(str.upper, unique))
lowercase = list(map(str.lower, unique))

print("Original sequence:", sequence)
print("Without duplicates:", unique)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)