# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):


        curr = head

        # length 
        leng = 0
        while curr:
            leng += 1
            curr = curr.next

        #remove head

        if n == leng:
            return head.next

        # position find 

        position = leng - n
        
        # remove node while

        curr = head
        i =1
        while i < position: 
            curr = curr.next
            i +=1

        curr.next = curr.next.next


        return head



        