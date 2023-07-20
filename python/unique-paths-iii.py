MOVES =[(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def is_valid(grid: List[List[int]], x: int, y: int) -> bool:
        if x < 0 or len(grid) <= x:
            return False
        if y < 0 or len(grid[0]) <= y:
            return False
        return 0 <= grid[x][y] and grid[x][y] < 3

    def dfs(grid: List[List[int]], x: int, y: int, steps: int, target_steps: int) -> int:
        if not Solution.is_valid(grid, x, y):
            return 0
        if grid[x][y] == 2:
            if steps == target_steps:
                return 1
            return 0
        valid_paths = 0
        original_value = grid[x][y]
        grid[x][y] = 3
        for move in MOVES:
            valid_paths += Solution.dfs(grid, x + move[0], y + move[1], steps + 1, target_steps)
        grid[x][y] = original_value
        return valid_paths

    def get_steps_and_start_position(grid: List[List[int]]) -> (int, int, int):
        target_steps = 0
        start_x, start_y = 0, 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    start_x, start_y = x, y
                if grid[x][y] == 0 or grid[x][y] == 1:
                    target_steps += 1
        return (target_steps, start_x, start_y)

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        target_steps, start_x, start_y = Solution.get_steps_and_start_position(grid)
        return Solution.dfs(grid, start_x, start_y, 0, target_steps)
