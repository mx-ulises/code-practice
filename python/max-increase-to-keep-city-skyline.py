class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[-1])
        row_maxes = [0] * n
        col_maxes = [0] * m
        for i in range(n):
            for j in range(m):
                row_maxes[i] = max(row_maxes[i], grid[i][j])
                col_maxes[j] = max(col_maxes[j], grid[i][j])
        heigh_diff = 0
        for i in range(n):
            for j in range(m):
                heigh_diff += min(row_maxes[i], col_maxes[j]) - grid[i][j]
        return heigh_diff
