# Problem 80: Find mode (most frequent element)
# Find and fix the error

def find_mode(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_count = 0
    mode = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = item
    return mode
numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Mode: {find_mode(numbers)}")
