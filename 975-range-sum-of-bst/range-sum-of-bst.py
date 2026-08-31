# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):

        if root is None:
            return 0

        #1 root.val < low:  # right

        if root.val < low:
            return self.rangeSumBST(root.right,low,high)


        #2   root.val > high #left
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)

        #3 low <= root.val <= high  add root
        # if low<= root.val <= high:
        return root.val + self.rangeSumBST(root.left,low,high) + (self.rangeSumBST(root.right,low,high))





