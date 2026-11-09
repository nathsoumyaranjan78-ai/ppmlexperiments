def next_fibonacci(x, y):
    return x + y


n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, next_fibonacci(a, b)