# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):

        output= []

        def preorder(root):
        # pre = root - left - right 
            if root == None:
                return 
            output.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return output

