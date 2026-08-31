# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        t = root

        # found the node

        if t.val == key:
            #case1:  No left child
            if t.left == None:
                return t.right
            if t.right == None:
                return t.left
            
            # Case2 : no child
            if t.left is None and t.right is None:
                return None

            #case3 2 children
            maxnode = t.left

            while maxnode.right:
                maxnode = maxnode.right

            t.val = maxnode.val
            t.left = self.deleteNode(t.left, maxnode.val)


        
        elif key < t.val:
            t.left = self.deleteNode(t.left,key)


        else: # key > t.val
            t.right = self.deleteNode(t.right,key)

        return t
    
        