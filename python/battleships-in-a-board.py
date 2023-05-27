class Solution:
    def remove_battleship(i: int, j: int, board: List[List[int]]) -> int:
        if i == len(board) or j == len(board[i]) or board[i][j] == ".":
            return 0
        board[i][j] = "."
        Solution.remove_battleship(i + 1, j, board)
        Solution.remove_battleship(i, j + 1, board)
        return 1

    def countBattleships(self, board: List[List[str]]) -> int:
        battleship_count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                battleship_count += Solution.remove_battleship(i, j, board)
        return battleship_count
