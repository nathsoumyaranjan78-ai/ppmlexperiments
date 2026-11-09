n = int(input("Enter the value of N: "))

for i in range(2, n):
    count1 = 0
    count2 = 0

    for j in range(1, i+1):
        if i % j == 0:
            count1 += 1

    for j in range(1, i+3):
        if (i+2) % j == 0:
            count2 += 1

    if count1 == 2 and count2 == 2 and i+2 <= n:
        print(i, i+2)