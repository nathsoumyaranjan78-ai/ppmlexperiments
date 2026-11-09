p = float(input("Enter percentage: "))

if p >= 90 and p <= 100:
    print("Grade O")
elif p >= 80:
    print("Grade A+")
elif p >= 70:
    print("Grade A")
elif p >= 60:
    print("Grade B")
elif p >= 50:
    print("Grade C")
elif p >= 40:
    print("Grade D")
elif p >= 0:
    print("Grade F")
else:
    print("Invalid percentage")