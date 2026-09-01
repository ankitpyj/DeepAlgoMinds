# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        first = [None]
        second = [None]
        prev = [None]

        def inorder(root):
            if root is None:
                return

            inorder(root.left)

            if prev[0] and prev[0].val > root.val:
                if first[0] is None:
                    first[0] = prev[0]
                second[0] = root

            prev[0] = root

            inorder(root.right)

        inorder(root)

        first[0].val, second[0].val = second[0].val, first[0].val