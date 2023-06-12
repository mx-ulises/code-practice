TILE_3_MAP = {
    ' ': [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ],
    '/': [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ],
    '\\': [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ],
}

MOVES = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

class Solution:
    def update_grid(grid: List[List[int]], x: int, c: str):
        start_i = x * 3
        if len(grid) == start_i:
            grid.extend([[], [], []])
        for i in range(start_i, len(grid)):
            grid[i].extend(TILE_3_MAP[c][i % 3])

    def get_grid_3(grid: List[str]) -> List[List[int]]:
        grid_3 = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                Solution.update_grid(grid_3, i, grid[i][j])
        return grid_3

    def valid_position(grid: List[List[int]], x: int, y: int) -> bool:
        if x < 0 or x == len(grid):
            return False
        if y < 0 or y == len(grid[x]):
            return False
        return grid[x][y] == 0

    def cover_region(grid: List[List[int]], x: int, y: int) -> int:
        if not Solution.valid_position(grid, x, y):
            return 0
        grid[x][y] = 1
        for move in MOVES:
            Solution.cover_region(grid, x + move[0], y + move[1])
        return 1

    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_3 = Solution.get_grid_3(grid)
        region_count = 0
        for i in range(len(grid_3)):
            for j in range(len(grid_3[i])):
                region_count += Solution.cover_region(grid_3, i, j)
        return region_count
