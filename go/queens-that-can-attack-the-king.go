// Declare a global 2D array
var DIRECTIONS = [8][2]int{
	{0, 1}, {0, -1}, {1, 0}, {-1, 0},
	{1, 1}, {1, -1}, {-1, 1}, {-1, -1},
}

var BOARD_SIZE = 8

func BuildQueenSet(queens [][]int) map[int]bool {
	queenSet := make(map[int]bool)
	for i := 0; i < len(queens); i++ {
		position := (10*queens[i][0] + queens[i][1])
		queenSet[position] = true
	}
	return queenSet
}

func IsKingAttacked(queenSet map[int]bool, king []int, direction [2]int) ([]int, bool) {
	x := king[0] + direction[0]
	y := king[1] + direction[1]
	isKingAttacked := false
	queen := []int{-1, -1}
	for 0 <= x && x < BOARD_SIZE && 0 <= y && y < BOARD_SIZE {
		position := 10*x + y
		if queenSet[position] {
			isKingAttacked = true
			queen[0] = x
			queen[1] = y
			break
		}
		x += direction[0]
		y += direction[1]
	}
	return queen, isKingAttacked
}

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	queenSet := BuildQueenSet(queens)
	queensAttacking := make([][]int, 0)
	for i := 0; i < len(DIRECTIONS); i++ {
		queen, isKingAttacked := IsKingAttacked(queenSet, king, DIRECTIONS[i])
		if isKingAttacked {
			queensAttacking = append(queensAttacking, queen)
		}
	}
	return queensAttacking
}
