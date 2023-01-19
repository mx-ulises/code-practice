MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def is_valid(i: int, j: int, grid: List[List[int]]) -> bool:
        if i < 0 or len(grid) <= i:
            return False
        if j < 0 or len(grid[0]) <= j:
            return False
        return grid[i][j] == 1

    def get_area(i: int, j: int, grid: List[List[int]]) -> int:
        area = 0
        s = [(i, j)]
        while s:
            i, j = s.pop()
            if Solution.is_valid(i, j, grid):
                grid[i][j] = 0
                area += 1
                for move in MOVES:
                    s.append((i + move[0], j + move[1]))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                max_area = max(max_area, Solution.get_area(i, j, grid))
        return max_area
