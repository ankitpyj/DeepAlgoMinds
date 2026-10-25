class Solution(object):
    def hasAlternatingBits(self, n):
        prev = n % 2
        n //= 2

        while n > 0:
            curr = n % 2

            if curr == prev:
                return False

            prev = curr
            n //= 2

        return True