# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            length = len(queue)

            for i in range(length):
                node=queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == length - 1:
                    result.append(node.val)

        return result


        


        