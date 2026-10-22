class Solution(object):
    def isPowerOfTwo(self, n):
        
        if n<=0:
            return False

        while n>1:
            rem = n%2
            if rem !=0:
                return False
            n=n//2

        return True
        