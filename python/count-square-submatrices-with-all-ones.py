MOVES = [(-1, 0), (0, -1), (-1, -1)]

class Solution:
    def position_value(matrix: List[List[int]], x: int, y: int) -> int:
        if x < 0 or y < 0:
            return 0
        return matrix[x][y]

    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        count = 0
        for i in range(n):
            for j in range(m):
                min_neighbor_size = 300
                if matrix[i][j] == 0:
                    continue
                for move in MOVES:
                    x = i + move[0]
                    y = j + move[1]
                    neighbor_size = Solution.position_value(matrix, x, y)
                    min_neighbor_size = min(neighbor_size, min_neighbor_size)
                matrix[i][j] = min_neighbor_size + 1
                count += matrix[i][j]
        return count
