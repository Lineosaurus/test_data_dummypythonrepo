# Dummy Python Script

# Calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Print the factorial of 5
print("Factorial of 5:", factorial(5))

# Print the first 10 Fibonacci numbers
fib_numbers = fibonacci(10)
print("Fibonacci Sequence:", fib_numbers)
