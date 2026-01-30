# Problem 96: Find two numbers that sum to target
# Find and fix the error

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None
numbers = [2, 7, 11, 15]
print(f"Indices: {two_sum(numbers, 9)}")
