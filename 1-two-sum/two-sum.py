class Solution(object):
    def twoSum(self, nums, target):
        map ={}

        for i,num in enumerate(nums):
            exist_check = target - num

            if exist_check in map:
                return [map[exist_check],i]

            map[num] = i


                
        