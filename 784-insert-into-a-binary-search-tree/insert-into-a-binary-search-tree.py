# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):


#  If root is None:
#     create a new node and return it
        if root is None:
            return TreeNode(val)

# If val < root.val:
#     insert into left subtree

        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root

# Else:
#     insert into right subtree

# Return root