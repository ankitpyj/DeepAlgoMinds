class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        freq = [0] * (n * n + 1)

        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1

        repeated = 0
        missing = 0

        for i in range(1, len(freq)):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i

        return [repeated, missing]