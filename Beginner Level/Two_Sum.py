def Two_Sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

# Test
print(Two_Sum([2, 7, 11, 15], 9))  # Outputs: [0, 1]
