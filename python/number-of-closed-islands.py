MOVES = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

class Solution:
    def is_valid(i: int, j: int, grid: List[List[int]]) -> bool:
        if i < 0 or len(grid) <= i:
            return False
        if j < 0 or len(grid[0]) <= j:
            return False
        if grid[i][j] == 1 or grid[i][j] == 2:
            return False
        return True

    def dfs_mark(i: int, j: int, grid: List[List[int]]) -> bool:
        if Solution.is_valid(i, j, grid):
            grid[i][j] = 2
            for move in MOVES:
                Solution.dfs_mark(i + move[0], j + move[1], grid)
            return True
        return False

    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            Solution.dfs_mark(i, 0, grid)
            Solution.dfs_mark(i, m - 1, grid)
        for j in range(m):
            Solution.dfs_mark(0, j, grid)
            Solution.dfs_mark(n - 1, j, grid)
        count = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if Solution.dfs_mark(i, j, grid):
                    count += 1
        return count
