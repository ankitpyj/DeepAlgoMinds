class Solution(object):
    def findTheDifference(self, s, t):
        ans = 0
        stringg = s+t
        for ch in stringg:
            ans ^= ord(ch)

        return chr(ans)