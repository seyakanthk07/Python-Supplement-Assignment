# Problem 100: Calculate average of nested lists
# Find and fix the error

def average_nested(nested_list):
    total_sum = 0
    count = 0
    for sublist in nested_list:
        for item in sublist:
            total_sum += item
            count += 1
    return total_sum / count if count != 0 else 0
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Average: {average_nested(data)}")
