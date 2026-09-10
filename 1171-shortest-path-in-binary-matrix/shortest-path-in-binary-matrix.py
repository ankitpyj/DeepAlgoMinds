from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1

        queue = deque()

        queue.append((0, 0,1))
    #    count =0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[0][0] == 0:
    #                 queue.append((i,j))
    #                 count =1 

        while queue:
            row , col,count  = queue.popleft()
            if row == m - 1 and col == n - 1:
                return count

            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col,count + 1))

        return -1








        