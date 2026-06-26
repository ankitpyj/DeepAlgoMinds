# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):

        store = []

        def list_add(root):

            if root is None:
                return

            store.append(root.val)

            list_add(root.left)
            list_add(root.right)

        list_add(root)

        store.sort()

        ans = float('inf')

        for i in range(1,len(store)):
            ans = min(ans,store[i] - store[i-1])

        return ans

