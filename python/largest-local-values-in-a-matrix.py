class Solution:
    def get_local_maximal(grid: List[List[int]], x, y):
        maximal = 0
        for i in range(3):
            for j in range(3):
                maximal = max(maximal, grid[x + i][y + j])
        return maximal

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new_grid = []
        for x in range(len(grid) - 2):
            new_grid.append([])
            for y in range(len(grid[-1]) - 2):
                maximal = Solution.get_local_maximal(grid, x, y)
                new_grid[-1].append(maximal)
        return new_grid
