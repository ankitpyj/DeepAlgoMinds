class Solution(object):
    def countSpecialIntegers(self, nums):
        block = {}

        for i in range(len(nums)):
            if i ==0 or nums[i] != nums[i-1]:
                block[nums[i]] = block.get(nums[i],0)+1

        ans = 0 
        for i in block:
            if block[i] ==1:
                ans +=1

        return ans