class Solution(object):
    def countBits(self, n):
        ans = []

        for i in range(n + 1):
            num = i
            count = 0

            while num > 0:
                rem = num % 2

                if rem == 1:
                    count += 1

                num //= 2

            ans.append(count)

        return ans