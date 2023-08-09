class Solution:
    def initialize_output(grid: List[List[int]]) -> List[List[int]]:
        output = []
        for row in grid:
            output.append([0] * len(row))
        return output

    def get_right_values(grid: List[List[int]], x: int, y: int):
        diagonal_elements = min(len(grid) - x, len(grid[0]) - y)
        right_values = defaultdict(lambda: 0)
        for offset in range(diagonal_elements):
            element = grid[x + offset][y + offset]
            right_values[element] += 1
        return right_values

    def compute_diagonal(grid: List[List[int]], output: List[List[int]], x: int, y: int):
        right_values = Solution.get_right_values(grid, x, y)
        left_values = defaultdict(lambda: 0)
        diagonal_elements = min(len(grid) - x, len(grid[0]) - y)
        for offset in range(diagonal_elements):
            element = grid[x + offset][y + offset]
            right_values[element] -= 1
            if right_values[element] == 0:
                del right_values[element]
            output[x + offset][y + offset] = abs(len(right_values) - len(left_values))
            left_values[element] += 1

    def compute_diagonals(grid: List[List[int]], output: List[List[int]]):
        Solution.compute_diagonal(grid, output, 0, 0)
        for i in range(1, len(grid)):
            Solution.compute_diagonal(grid, output, i, 0)
        for j in range(1, len(grid[0])):
            Solution.compute_diagonal(grid, output, 0, j)

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        output = Solution.initialize_output(grid)
        Solution.compute_diagonals(grid, output)
        return output
