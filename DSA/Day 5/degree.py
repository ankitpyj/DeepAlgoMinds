class Solution:
    def findShortestSubArray(self, nums):

        freq = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):

            if num not in first:
                first[num] = i

            last[num] = i
            freq[num] = freq.get(num, 0) + 1

        degree = max(freq.values())

        ans = len(nums)

        for num in freq:

            if freq[num] == degree:
                length = last[num] - first[num] + 1
                ans = min(ans, length)

        return ans
    

nums = [1,2,2,3,1]
ob = Solution()
print(ob.findShortestSubArray(nums))