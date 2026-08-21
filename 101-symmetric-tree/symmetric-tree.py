# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def mirror(p,q):

            if p == None and q== None:
                return True
            
            if p == None or q == None:
                return False

            if p.val != q.val:
                return False

            if p.val == q.val:
                left = mirror(p.left,q.right)
                right =mirror(p.right,q.left)

                return left and right

        return mirror(root.left,root.right)
