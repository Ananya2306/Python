def Max_of_Three_Num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test
print(Max_of_Three_Num(3, 7, 5))  # Outputs: 7
print(Max_of_Three_Num(10, 2, 15))  # Outputs: 15