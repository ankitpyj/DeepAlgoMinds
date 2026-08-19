class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        while left <= right:
            sum =0
            mid = (left + right)//2
            k = mid

            for i in piles:
                if i % k ==0:
                    sum += (i//k)
                else:
                    sum += (i//k)+1

            if sum <= h:
                right = mid-1

            else: # sum>=h
                left = mid +1

        return left





