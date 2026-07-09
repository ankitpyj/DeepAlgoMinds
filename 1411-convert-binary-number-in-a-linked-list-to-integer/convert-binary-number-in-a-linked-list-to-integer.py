# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):

        List1 = []

        while head:
            List1.append(head.val)
            head = head.next

        ans = 0
        n = len(List1)
        for i in range(n):
            ans += List1[i] * (2**(n-i-1))

        return ans

        
        