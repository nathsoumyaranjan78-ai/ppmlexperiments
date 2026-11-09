n = int(input("Enter a 3-digit number: "))

if n >= 100 and n <= 999:
    print("Prime factors are:")

    i = 2

    while n > 1:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i = i + 1
else:
    print("Please enter a 3-digit number")