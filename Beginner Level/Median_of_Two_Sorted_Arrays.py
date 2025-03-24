def Median_of_Sorted_Arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)
    if length % 2 == 0:
        return (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        return nums[length // 2]

# Test
print(Median_of_Sorted_Arrays([1, 3], [2]))         # Outputs: 2.0
print(Median_of_Sorted_Arrays([1, 2], [3, 4]))      # Outputs: 2.5
"""
 # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = total_len // 2
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1  # Move right
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1  # Move left
            else:
                # i is perfect, now find the median
                if i == 0: left_max = nums2[j - 1]
                elif j == 0: left_max = nums1[i - 1]
                else: left_max = max(nums1[i - 1], nums2[j - 1])
                
                if total_len % 2 == 1:
                    return left_max  # Odd case
                
                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])
                
                return (left_max + right_min) / 2.0  # Even case
"""