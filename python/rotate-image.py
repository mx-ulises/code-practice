class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        offset = 0
        while offset <= n:
            for i in range(n - offset):
                aux = matrix[offset + i][n]
                matrix[offset + i][n] = matrix[offset][offset + i]
                matrix[offset][offset + i] = matrix[n - i][offset]
                matrix[n - i][offset] = matrix[n][n - i]
                matrix[n][n - i] = aux
            offset += 1
            n -= 1
