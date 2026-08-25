# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        maxi = 0

        queue = deque([(root,0)])
        

        while queue:
            store_value = []

            for i in range(len(queue)):
                node,indx = queue.popleft()

                store_value.append(indx)

                if node.left:
                    queue.append((node.left, 2*indx + 1))

                if node.right:
                    queue.append((node.right, 2*indx + 2))

            width = store_value[-1] - store_value[0] +1
            maxi = max(maxi,width)


        return maxi


        
        