DIRECTIONS = [
    (1, 1), (-1, -1), (1, -1), (-1, 1),
    (0, 1), (0, -1), (1, 0), (-1, 0),
]

LIMIT_X, LIMIT_Y = 8, 8

class Solution:
    def is_king_attacked(queens: List[List[int]], king: List[int], x: int, y: int) -> (int, int):
        current_x, current_y = king[0] + x, king[1] + y
        while (0 <= current_x < LIMIT_X) and (0 <= current_y < LIMIT_Y):
            if (current_x, current_y) in queens:
                return (current_x, current_y)
            current_x += x
            current_y += y
        return None

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens_count = []
        queens = {(x, y) for x, y in queens}
        for x, y in DIRECTIONS:
            queen = Solution.is_king_attacked(queens, king, x, y)
            if queen != None:
                queens_count.append(queen)
        return queens_count
