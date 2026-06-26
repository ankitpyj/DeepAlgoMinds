# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        # we find the root so sbse pehle we find root -- middle , addnode ko ,   left  , right 
        def bst(nums):

            if not nums: #if nums == None
                return None


            mid = len(nums) //2

            root = TreeNode(nums[mid])

            root.left = bst(nums[:mid])
            root.right = bst(nums[mid+1:])

            return root

        return bst(nums)
        

        