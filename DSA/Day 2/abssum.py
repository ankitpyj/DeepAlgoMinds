def maxAbsoluteSum(nums):
    curr_max = nums[0]
    max_sum = nums[0]

    curr_min = nums[0]
    min_sum = nums[0]

    for i in range(1, len(nums)):

        # Maximum subarray sum (Kadane)
        curr_max = max(nums[i], curr_max + nums[i])
        max_sum = max(max_sum, curr_max)

        # Minimum subarray sum (Reverse Kadane)  
        curr_min = min(nums[i], curr_min + nums[i])
        min_sum = min(min_sum, curr_min)

    return max(max_sum, abs(min_sum))


nums = [2,-5,1,-4,3,-2]
print(maxAbsoluteSum(nums))
    
nums = [1,-3,2,3,-4]
print(maxAbsoluteSum(nums))