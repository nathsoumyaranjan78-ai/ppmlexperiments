n = int(input("Enter a number: "))

temp = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")