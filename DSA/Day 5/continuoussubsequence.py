class Solution:
    def findLengthOfLCIS(self, nums):

        if not nums:
            return 0

        curr = 1   #current increasing length
        ans = 1        # maximum length found

        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                curr += 1
            else:
                curr = 1

            ans = max(ans, curr)

        return ans