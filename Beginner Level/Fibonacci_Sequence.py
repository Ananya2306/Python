def Fibonacci_Sequence(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Test
Fibonacci_Sequence(7)  # Outputs: 0 1 1 2 3 5 8
