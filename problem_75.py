# Problem 75: Check if parentheses are balanced
# Find and fix the error

def are_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    match = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
expr = "((a + b) * (c - d))"
print(f"Balanced: {are_balanced(expr)}")
