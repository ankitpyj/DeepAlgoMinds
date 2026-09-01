# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def rev_inorder(root):#bcoz curr + sum of all keys greater than original key) - right 
            
            nonlocal total
            if not root:
                return

            rev_inorder(root.right)

            total += root.val
            root.val = total

            rev_inorder(root.left)

        rev_inorder(root)

        return root

        