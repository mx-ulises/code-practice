VALID_LAND = 3
WATER = 0
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def merge_grid(grid1: List[List[int]], grid2: List[List[int]]):
        n, m = len(grid1), len(grid1[0])
        for i in range(n):
            for j in range(m):
                grid1[i][j] += grid2[i][j] * 2

    def is_water(grid: List[List[int]], x: int, y: int) -> bool:
        if x < 0 or x == len(grid):
            return True
        if y < 0 or y == len(grid[0]):
            return True
        if grid[x][y] & 2 == WATER:
            return True
        return False

    def get_valid_island(grid: List[List[int]], x: int, y: int) -> (int, bool):
        if Solution.is_water(grid, x, y):
            return (0, True)
        is_valid_island = grid[x][y] == VALID_LAND
        grid[x][y] = WATER
        for move in MOVES:
            is_valid_island &= Solution.get_valid_island(grid, x + move[0], y + move[1])[1]
        return (1, is_valid_island)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Solution.merge_grid(grid1, grid2)
        sub_islands_count = 0
        n, m = len(grid1), len(grid1[0])
        for i in range(n):
            for j in range(m):
                count, is_valid_island = Solution.get_valid_island(grid1, i, j)
                if is_valid_island:
                    sub_islands_count += count
        return sub_islands_count
