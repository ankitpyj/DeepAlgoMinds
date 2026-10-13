class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        #obstacle h first 0,0 
        if obstacleGrid[0][0] == 1:
            return 0
        
        #0,0 jane k liye one way
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                
                #obstacle aagya toh 0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                elif i > 0 or j > 0:

                    top = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0

                    dp[i][j] = top + left

        return dp[m - 1][n - 1]