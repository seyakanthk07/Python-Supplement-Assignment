# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth(lst, n):
    if n < 0 or n >= len(lst):
        return lst
    return lst[:n] + lst[n+1:]

numbers = [1, 2, 3, 4, 5]
result = remove_nth(numbers, 2)

print(f"After removing: {result}")