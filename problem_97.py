# Problem 97: Remove element from list
# Find and fix the error

def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

numbers = [3, 2, 2, 3, 4, 5]
length = remove_element(numbers, 3)
print(f"New length: {length}")
print(f"Modified list: {numbers[:length]}")
