# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def checkbst(root,low,high):

            if root is None:
                return True

            if root.val <= low or root.val >= high:
                return False

            left = checkbst(root.left,low,root.val)
            right = checkbst(root.right,root.val,high)

            return left and right
        
        return checkbst(root,float('-inf'),float('inf'))