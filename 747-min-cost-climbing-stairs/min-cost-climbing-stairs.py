class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2,n+1):
            # merko i p jane k liye -- 2 ways -- ya toh meh i-1 seh ya meh i-2
            # eg i =2 toh 2 ways -- ya  1 seh 2   or    0 seh 2

            dp[i] = min(dp[i-1] + cost[i-1] , dp[i-2] + cost[i-2])

        return dp[n]

        

            