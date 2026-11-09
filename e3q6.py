s = input("Enter a string: ")

result = ""

for i in s:
    if i not in result:
        result = result + i

print("String after removing duplicates:", result)