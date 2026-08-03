class Solution(object):
    def containsDuplicate(self, nums):
        dupli= set(nums)

        if len(dupli) < len(nums):
            return True
        return False


        