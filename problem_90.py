# Problem 90: Find median of a list
# Find and fix the error

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median
numbers = [1, 3, 5, 7, 9]
print(f"Median: {find_median(numbers)}")
