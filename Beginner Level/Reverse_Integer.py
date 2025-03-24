def Reverse_Integer(x):
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1])  # Reverse the integer as a string
    if rev > 2**31 - 1:  # 32-bit integer limit
        return 0
    return rev * sign

# Test
print(Reverse_Integer(123))  # Outputs: 321
print(Reverse_Integer(-123))  # Outputs: -321
