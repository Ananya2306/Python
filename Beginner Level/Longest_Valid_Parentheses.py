def Longest_Valid_Parentheses(s):
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

# Test
print(Longest_Valid_Parentheses(")()())"))  # Outputs: 4
print(Longest_Valid_Parentheses("(()"))     # Outputs: 2
