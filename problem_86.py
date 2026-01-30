# Problem 86: Find sum of matrix diagonals
# Find and fix the error

def diagonal_sum(matrix):
    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][i]  # Primary diagonal
        total += matrix[i][n - 1 - i]  # Secondary diagonal
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]  # Subtract the middle element if n is odd
    return total

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Diagonal sum: {diagonal_sum(mat)}")
