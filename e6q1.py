# Program to group similar elements in a matrix using functions

def create_matrix(rows, cols):
    matrix = []

    print("Enter the matrix elements:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def group_elements(matrix):
    # Convert matrix into a single list
    elements = []

    for row in matrix:
        elements.extend(row)

    # Group similar elements
    grouped = []
    visited = set()

    for element in elements:
        if element not in visited:
            count = elements.count(element)
            grouped.extend([element] * count)
            visited.add(element)

    return grouped


def make_matrix(grouped, rows, cols):
    result = []
    index = 0

    for i in range(rows):
        result.append(grouped[index:index + cols])
        index += cols

    return result


def display_matrix(matrix):
    for row in matrix:
        print(row)


# Main program
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = create_matrix(rows, cols)

grouped = group_elements(matrix)

result = make_matrix(grouped, rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nMatrix after grouping similar elements:")
display_matrix(result)
