#program objective is to write a program that uses nested for loops to add two matrices using nested

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions for addition."

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Perform matrix addition using nested for loops
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Define two matrices as lists of lists
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Add the matrices using the add_matrices function
result_matrix = add_matrices(matrix1, matrix2)

# Print the result matrix
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result Matrix:")
    for row in result_matrix:
        print(row)
