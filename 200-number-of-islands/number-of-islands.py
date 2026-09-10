from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for i in range(m):
            for j in range(n):

                # Found a NEW island
                if grid[i][j] == "1":
                    count += 1

                    queue = deque()
                    queue.append((i, j))

                    # Mark as visited
                    grid[i][j] = "0"

                    while queue:
                        row, col = queue.popleft()

                        for dr, dc in directions:
                            new_row = row + dr
                            new_col = col + dc

                            if (0 <= new_row < m and
                                0 <= new_col < n and
                                grid[new_row][new_col] == "1"):

                                grid[new_row][new_col] = "0"
                                queue.append((new_row, new_col))

        return count