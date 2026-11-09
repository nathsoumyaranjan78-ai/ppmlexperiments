s = input("Enter a word: ")

rev = s[::-1]

if s == rev:
    print("Palindrome word")
else:
    print("Not a palindrome word")