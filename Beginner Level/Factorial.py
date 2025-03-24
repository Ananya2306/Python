def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Factorial(n - 1)

# Test
print(Factorial(5))  # Outputs: 120 (5 * 4 * 3 * 2 * 1)
print(Factorial(0))  # Outputs: 1
