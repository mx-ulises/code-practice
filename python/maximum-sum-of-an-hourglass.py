class Solution:
    def get_grid_sum(grid, x, y):
        grid_sum = grid[x][y] + grid[x][y + 1] + grid[x][y + 2]
        grid_sum += grid[x + 1][y + 1]
        grid_sum += grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]
        return grid_sum

    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                max_sum = max(max_sum, Solution.get_grid_sum(grid, i, j))
        return max_sum
