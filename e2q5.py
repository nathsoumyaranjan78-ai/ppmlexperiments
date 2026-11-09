s = input("Enter a string: ")

rev = s[::-1]

vowels = 0
consonants = 0

for i in s:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Reversed string =", rev)
print("Number of vowels =", vowels)
print("Number of consonants =", consonants)