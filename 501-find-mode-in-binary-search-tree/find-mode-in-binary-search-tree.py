# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):

        store = {}

        def dic_store(root):

            if root is None:
                return 

            
            # store[root.val] +=1

            if root.val in store:
                store[root.val] += 1
            else:
                store[root.val] = 1
            dic_store(root.left)
            dic_store(root.right)

        dic_store(root)
        
        ans = []

        maxx= max(store.values())
        
        for key, value in store.items():
            if value == maxx:
                ans.append(key)

        return ans

 



        