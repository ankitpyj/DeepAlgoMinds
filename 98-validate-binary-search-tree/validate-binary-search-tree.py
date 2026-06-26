# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def check_bst(root, start, end):

            if root is None:
                return True

            if root.val <= start or root.val >= end:
                return False

            a = check_bst(root.left, start, root.val)
            b = check_bst(root.right, root.val, end)

            return a and b

        return check_bst(root, float('-inf'), float('inf'))