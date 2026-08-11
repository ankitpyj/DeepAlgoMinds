class Solution(object):
    def getIntersectionNode(self, headA, headB):

        sett = set()

        while headA:
            sett.add(headA)
            headA = headA.next

        while headB:
            if headB in sett:
                return headB
            headB = headB.next

        return None


#         currA = headA
#         currB = headB

#         lenA = 0
#         while currA:
#             lenA += 1
#             currA = currA.next

#         lenB = 0    
#         while currB:
#             lenB += 1
#             currB = currB.next

#         currA = headA
#         currB = headB

#         if lenA > lenB:
#             skip = lenA - lenB

#             for _ in range(skip):
#                 currA = currA.next

#         else:
#             skip = lenB - lenA

#             for _ in range(skip):
#                 currB = currB.next

#         while currA != currB:
#             currA = currA.next
#             currB = currB.next

#         return currA