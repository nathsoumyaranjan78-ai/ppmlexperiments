# Program to find the transpose of an n*n matrix using functions

def input_matrix(n):
    matrix = []

    print("Enter the matrix elements:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(row)


def transpose_matrix(matrix, n):
    transpose = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        transpose.append(row)

    return transpose


# Main program
n = int(input("Enter the order of matrix: "))

matrix = input_matrix(n)

print("\nOriginal Matrix:")
display_matrix(matrix)

transpose = transpose_matrix(matrix, n)

print("\nTranspose of Matrix:")
display_matrix(transpose)