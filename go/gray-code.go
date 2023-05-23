func GetMoves(n int) []int {
    moves := make([]int, 0)
    move := 1
    for i := 0; i < n; i++ {
        moves = append(moves, move)
        move *= 2
    }
    return moves
}

func grayCode(n int) []int {
    moves := GetMoves(n)
    output := make([]int, 0)
    visited := make(map[int]bool)
    visited[0] = true;
    s := make([]int, 1)
    for 0 < len(s) {
        x := s[len(s) - 1]
        s = s[:len(s) - 1]
        output = append(output, x)
        for i := 0; i < n; i++ {
            y := x ^ moves[i]
            if visited[y] != true {
                visited[y] = true
                s = append(s, y)
                break;
            }
        }
    }
    return output
}
