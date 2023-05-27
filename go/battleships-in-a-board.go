func RemoveBattleship(i int, j int, board [][]byte) int {
    if i == len(board) || j == len(board[i]) || board[i][j] == '.' {
        return 0
    }
    board[i][j] = '.'
    RemoveBattleship(i + 1, j, board)
    RemoveBattleship(i, j + 1, board)
    return 1
}

func countBattleships(board [][]byte) int {
    ballteshipCount := 0
    for i :=0; i < len(board); i++ {
        for j := 0; j < len(board[i]); j++ {
            ballteshipCount += RemoveBattleship(i, j, board)
        }
    }
    return ballteshipCount
}
