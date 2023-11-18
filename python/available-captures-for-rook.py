MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def get_rock_position(board: List[List[str]]) -> (int, int):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return (i, j)
        return None

    def can_capture(board: List[List[str]], rock_position: Tuple[int], move: Tuple[int]) -> bool:
        x, y = rock_position
        while 0 <= x and x < 8 and 0 <= y and y < 8:
            if board[x][y] == 'p':
                return True
            if board[x][y] == 'B':
                return False
            x += move[0]
            y += move[1]
        return False

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rock_position = Solution.get_rock_position(board)
        captures = 0
        for move in MOVES:
            if Solution.can_capture(board, rock_position, move):
                captures += 1
        return captures
