class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            if len(set(matrix[i])) < n:
                return False
            if len(set([matrix[j][i] for j in range(n)])) < n:
                return False
        return True
