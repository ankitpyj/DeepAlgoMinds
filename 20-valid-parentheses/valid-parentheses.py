class Solution(object):
    def isValid(self, s):
        check = {'(' : ')', '{': '}', '[' : ']'}
        # check = {')' : '(', '}': '{', ']' : '['}
        stack = []

        for i in s:
            if i in check:
                stack.append(i)
            else:
                # False wale First

                if len(stack) == 0:
                    return False 
                if check[stack[-1]] != i:
                    return False

                stack.pop() 

        # stack empty honi chahiye         
        return len(stack) == 0



