# Problem 81: Check if string has balanced brackets
# Find and fix the error

def balanced_brackets(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    opening_brackets = set(bracket_map.values())
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0
expr = "{[a + b] * (c + d)}"
print(f"Balanced: {balanced_brackets(expr)}")