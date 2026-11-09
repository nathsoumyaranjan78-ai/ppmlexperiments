n = input("Enter a 5-digit number: ")

if len(n) == 5 and n.isdigit():
    print("Digits at odd locations:")

    for i in range(0, 5, 2):
        print(n[i])
else:
    print("Please enter a valid 5-digit number")