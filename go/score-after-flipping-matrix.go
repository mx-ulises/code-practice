func FlipRow(grid [][]int, i int) {
	for j := 0; j < len(grid[i]); j++ {
		grid[i][j] ^= 1
	}
}

func MaximizeRows(grid [][]int) {
	for i := 0; i < len(grid); i++ {
		if grid[i][0] == 0 {
			FlipRow(grid, i)
		}
	}
}

func SumCol(grid [][]int, j int) int {
	oneCount := 0
	for i := 0; i < len(grid); i++ {
		oneCount += grid[i][j]
	}
	return oneCount
}

func FlipCol(grid [][]int, j int) {
	for i := 0; i < len(grid); i++ {
		grid[i][j] ^= 1
	}
}

func MaximizeCols(grid [][]int) {
	for j := 0; j < len(grid[0]); j++ {
		oneCount := SumCol(grid, j)
		zeroCount := len(grid) - oneCount
		if oneCount < zeroCount {
			FlipCol(grid, j)
		}
	}
}

func GetRowScore(grid [][]int, i int) int {
	rowScore := 0
	for j := 0; j < len(grid[i]); j++ {
		rowScore = (rowScore << 1) | grid[i][j]
	}
	return rowScore
}

func GetScore(grid [][]int) int {
	score := 0
	for i := 0; i < len(grid); i++ {
		score += GetRowScore(grid, i)
	}
	return score
}

func matrixScore(grid [][]int) int {
	MaximizeRows(grid)
	MaximizeCols(grid)
	return GetScore(grid)
}
