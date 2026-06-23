# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        # p and q = NONE == True

        if p == None and q == None:
            return True 

        # p = none ya fir q = none dono meh seh ek none == false
        if p == None or q == None:
            return False

        #values is different == false

        if p.val != q.val:
            return False

        # values is same vist left and right
        if p.val == q.val:

            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)

            return left and right












        # outputp= []

        # def prep(p):

        #     if p == None:
        #         return 

        #     outputp.append(p.val)
        #     prep(p.left)
        #     prep(p.right)
        
        # prep(p)


        # outputq = []

        # def preq(q):

        #     if q == None:
        #         return 

        #     outputq.append(q.val)
        #     preq(q.left)
        #     preq(q.right)  

        # preq(q)

        # return outputp == outputq     




        