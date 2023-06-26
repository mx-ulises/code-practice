func equalPairs(grid [][]int) int {
	rows := make(map[string]int)
	columns := make(map[string]int)
	n := len(grid)
	for i := 0; i < n; i++ {
		row := ""
		column := ""
		for j := 0; j < n; j++ {
			row += strconv.Itoa(grid[i][j]) + "_"
			column += strconv.Itoa(grid[j][i]) + "_"
		}
		rows[row] += 1
		columns[column] += 1
	}
	pairs := 0
	for row := range rows {
		pairs += rows[row] * columns[row]
	}
	return pairs
}
