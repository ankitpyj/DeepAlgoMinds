class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        sum = nums[0]

        for i in range(1,len(nums)):
            sum = max(nums[i],nums[i]+sum)
            max_sum = max(max_sum,sum)

        return max_sum
        