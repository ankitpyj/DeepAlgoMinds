class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # dictt = {')' : '('}
        # stack = []
        # string = ""
        # for i in range(0 ,len(s)):
        #     stack.append(s[i])

        #     if s[i] in dictt.values():
        #         for i in range(0,2):
        #             string += stack.pop() + string

        # return string
        
        string = ""
        balance = 0

        for ch in s:
            if ch == "(":
                if balance >0:
                    string += ch
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    string += ch
        return string

            



        