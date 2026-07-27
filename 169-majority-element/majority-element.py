class Solution(object):
    def majorityElement(self, nums):
        
        freq= {}

        for i in nums:
            if i in freq:
                freq[i] += 1

            else:
                freq[i] = 1
        
        midd = len(nums)//2

        for j in freq:
            if freq[j] > midd:
                return j
            