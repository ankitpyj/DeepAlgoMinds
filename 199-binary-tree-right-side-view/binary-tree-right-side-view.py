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

        levelstore ={}

        queue = deque([(root,0)])

        while queue:

            for i in range(len(queue)):
                node,level = queue.popleft()

                levelstore[level] =  node.val

                if node.left:
                    queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

        return list(levelstore.values())



        


        