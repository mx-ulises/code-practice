class Solution:
    def fill_row(matrix: List[List[int]], i: int) -> None:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    def fill_column(matrix: List[List[int]], j: int) -> None:
        for i in range(len(matrix)):
            matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_column_is_zero = False
        first_row_is_zero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        first_row_is_zero = True
                    if j == 0:
                        first_column_is_zero = True
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                Solution.fill_row(matrix, i)
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                Solution.fill_column(matrix, j)
        if first_column_is_zero:
            Solution.fill_column(matrix, 0)
        if first_row_is_zero:
            Solution.fill_row(matrix, 0)
