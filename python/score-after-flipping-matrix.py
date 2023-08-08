class Solution:

    def get_row_score(row: List[int]) -> int:
        row_score = 0
        for i in range(len(row)):
            row_score = (row_score << 1) | row[i]
        return row_score


    def get_score(grid: List[List[int]]) -> int:
        score = 0
        for row in grid:
            score += Solution.get_row_score(row)
        return score


    def toggle_row(row: List[int]):
        for i in range(len(row)):
            row[i] ^= 1


    def maximize_rows(grid: List[List[int]]):
        for row in grid:
            if row[0] == 0:
                Solution.toggle_row(row)


    def toggle_column(grid: List[List[int]], i: int):
        for j in range(len(grid)):
            grid[j][i] ^= 1


    def maximize_columns(grid: List[List[int]]):
        row_num = len(grid)
        for i in range(len(grid[0])):
            one_count = sum([grid[j][i] for j in range(row_num)])
            zero_count = row_num - one_count
            if one_count < zero_count:
                Solution.toggle_column(grid, i)


    def matrixScore(self, grid: List[List[int]]) -> int:
        Solution.maximize_rows(grid)
        Solution.maximize_columns(grid)
        return Solution.get_score(grid)
