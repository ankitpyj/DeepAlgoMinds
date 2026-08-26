# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        if root is None:
            return None
        
        listt =[]

        def inorderr(root):
            if root is None:
                return

            inorderr(root.left)
            listt.append(root.val)
            inorderr(root.right)
        inorderr(root)
        return listt[k-1]
        