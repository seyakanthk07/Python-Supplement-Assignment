# Problem 73: Find maximum difference between elements
# Find and fix the error

def max_difference(arr):
    if len(arr) < 2:
        return 0
    min_elem = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - min_elem > max_diff:
            max_diff = arr[i] - min_elem
        if arr[i] < min_elem:
            min_elem = arr[i]
    return max_diff
numbers = [7, 1, 5, 3, 6, 4]
print(f"Max difference: {max_difference(numbers)}")
