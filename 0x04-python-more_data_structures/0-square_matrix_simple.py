#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []  # Create an empty list to store the new matrix


    for row in matrix:  # Iterate through each row in the input matrix
        new_row = []  # Create an empty list for the new row
        for elem in row:  # Iterate through each element in the row
            new_row.append(elem ** 2)  # Square the element and add it to the new row
        new_matrix.append(new_row)  # Add the new row to the new matrix


    return new_matrix  # Return the new matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
