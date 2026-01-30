# Problem 34: Copy a list
# Find and fix the error

original = [1, 2, 3, 4, 5]
copy = original.copy()
# copy = original  # This line was incorrect; it created a reference instead of a copy
copy.append(6)
print(f"Original: {original}")
print(f"Copy: {copy}")
