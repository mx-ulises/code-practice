class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        output_matrix = [[0] * m for _ in range(n)]
        col_start_index = 0
        for i in range(n):
            for j in range(col_start_index, m):
                minimal_substraction = min(rowSum[i], colSum[j])
                rowSum[i] -= minimal_substraction
                colSum[j] -= minimal_substraction
                output_matrix[i][j] += minimal_substraction
                if colSum[j] == 0:
                    col_start_index = j
                if rowSum[i] == 0:
                    break
        return output_matrix
