class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            exist = target - nums[i]

            if exist in hashmap:
                return [i,hashmap[exist]]

            hashmap[nums[i]] = i