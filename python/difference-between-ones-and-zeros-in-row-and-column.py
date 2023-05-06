class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ones_row = [0] * n
        ones_col = [0] * m
        for i in range(n):
            for j in range(m):
                is_one = grid[i][j]
                ones_row[i] += is_one
                ones_col[j] += is_one
        for i in range(n):
            for j in range(m):
                grid[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - n - m
        return grid
