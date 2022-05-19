NB = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid(i, j, grid):
    n, m = len(grid), len(grid[0])
    if i < 0 or n <= i:
        return False
    if j < 0 or m <= j:
        return False
    if grid[i][j] == 0:
        return False
    return True

def erase_border(i, j, grid):
    if not is_valid(i, j, grid):
        return
    grid[i][j] = 0
    for offset_i, offset_j in NB:
        erase_border(i + offset_i, j + offset_j, grid)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            erase_border(i, 0, grid)
            erase_border(i, m - 1, grid)
        for j in range(m):
            erase_border(0, j, grid)
            erase_border(n - 1, j, grid)
        return sum([sum(row) for row in grid])
