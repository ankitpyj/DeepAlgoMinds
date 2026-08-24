class Solution(object):
    def findPeakElement(self, nums):

        hashmap= {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        nums.sort()

        last = nums[len(nums)-1]

        return hashmap[last]

        