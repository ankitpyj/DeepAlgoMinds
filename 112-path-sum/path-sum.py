# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root == None:
            return False

        #leaf 

        if root.left == None and root.right == None:
            return targetSum == root.val

        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum - root.val)

        