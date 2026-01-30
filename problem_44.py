# Problem 44: Print Fibonacci sequence
# Find and fix the error

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
print(f"First 10 Fibonacci numbers: {fibonacci(10)}")