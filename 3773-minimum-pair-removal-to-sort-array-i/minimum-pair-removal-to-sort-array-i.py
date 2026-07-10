class Solution(object):
    def minimumPairRemoval(self, nums):
        count = 0

        while True:

            # Check if the array is non-decreasing
            sortedArray = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    sortedArray = False
                    break

            if sortedArray:
                return count

            minsum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                curr = nums[i] + nums[i + 1]

                if curr < minsum:
                    minsum = curr
                    idx = i

            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)
            count += 1