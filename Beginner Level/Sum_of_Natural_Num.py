def Sum_of_Natural_Num(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# Test
print(Sum_of_Natural_Num(5))  # Outputs: 15 (1 + 2 + 3 + 4 + 5)
print(Sum_of_Natural_Num(10)) # Outputs: 55
