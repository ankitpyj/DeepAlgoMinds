class Solution(object):
    def containsDuplicate(self, nums):

        ans = set()

        for i in nums:
            if i in ans:
                return True
            ans.add(i)
        return False

        