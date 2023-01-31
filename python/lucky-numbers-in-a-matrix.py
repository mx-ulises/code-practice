class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        rows, cols = defaultdict(lambda: []), defaultdict(lambda: [])
        for i in range(n):
            for j in range(m):
                rows[i].append(matrix[i][j])
                cols[j].append(matrix[i][j])
        rows = set([min(rows[i]) for i in rows])
        cols = set([max(cols[j]) for j in cols])
        return list(rows & cols)
