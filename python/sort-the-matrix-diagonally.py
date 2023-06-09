class Solution:
    def get_diagonal(mat: List[List[int]], x: int, y: int) -> List[int]:
        diagonal = []
        while x < len(mat) and y < len(mat[x]):
            diagonal.append(mat[x][y])
            x += 1
            y += 1
        return diagonal

    def fill_diagonal(mat: List[List[int]], x: int, y: int, diagonal: List[int]):
        for i in range(len(diagonal)):
            mat[x + i][y + i] = diagonal[i]

    def sort_diagonal(mat: List[List[int]], x: int, y: int):
        diagonal = Solution.get_diagonal(mat, x, y)
        diagonal.sort()
        Solution.fill_diagonal(mat, x, y, diagonal)

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for x in range(len(mat)):
            Solution.sort_diagonal(mat, x, 0)
        for y in range(1, len(mat[0])):
            Solution.sort_diagonal(mat, 0, y)
        return mat
