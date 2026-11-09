s = input("Enter a string: ")

n = len(s)

if n % 2 == 0:
    first = s[:n//2]
    second = s[n//2:]

    if first == second:
        print("Symmetrical string")
    else:
        print("Not symmetrical string")
else:
    print("Not symmetrical string")

if s == s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")