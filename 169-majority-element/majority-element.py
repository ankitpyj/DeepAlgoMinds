class Solution(object):
    def majorityElement(self, nums):

        candidate = nums[0]
        count = 1

        for num in nums[1:]:

            if candidate == num:
                count +=1

            else:
                count -=1

            if count ==0:
                candidate = num
                count = 1

        return candidate

        