# Program to find sum of rows and columns of a 3x3 matrix

def input_matrix():
    matrix = []

    print("Enter the elements of 3x3 matrix:")
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def row_sum(matrix):
    print("\nMatrix with row sums:")

    for i in range(3):
        total = sum(matrix[i])
        print(matrix[i], "=", total)


def column_sum(matrix):
    print("\nColumn sums:")

    for j in range(3):
        total = 0

        for i in range(3):
            total = total + matrix[i][j]

        print("Column", j + 1, "=", total)


# Main program
matrix = input_matrix()

row_sum(matrix)
column_sum(matrix)