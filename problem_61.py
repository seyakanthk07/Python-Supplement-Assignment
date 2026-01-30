# Problem 61: Find pairs with given sum
# Find and fix the error

def find_pairs(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

numbers = [1, 2, 3, 4, 5]
print(f"Pairs with sum 5: {find_pairs(numbers, 5)}")
