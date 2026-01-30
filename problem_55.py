# Problem 55: Count frequency of each element
# Find and fix the error

def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Frequency: {count_frequency(numbers)}")
