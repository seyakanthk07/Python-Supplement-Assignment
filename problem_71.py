# Problem 71: Transpose a matrix
# Find and fix the error

def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed

mat = [[1, 2, 3], [4, 5, 6]]
print(f"Transposed: {transpose(mat)}")
