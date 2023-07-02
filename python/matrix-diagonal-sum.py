class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - i - 1]
        if n & 1 == 1:
            n = n >> 1
            total -= mat[n][n]
        return total
