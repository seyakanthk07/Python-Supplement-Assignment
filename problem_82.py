# Problem 82: Remove adjacent duplicates
# Find and fix the error

def remove_adjacent_duplicates(text):
    if not text:
        return text
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)

s = "programming"
print(f"After removal: {remove_adjacent_duplicates(s)}")
