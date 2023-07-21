func deleteGreatestValue(grid [][]int) int {
	output := 0
	for _, row := range grid {
		sort.Ints(row)
	}
	for i := 0; i < len(grid[0]); i++ {
		maximal := 0
		for _, row := range grid {
			if maximal < row[i] {
				maximal = row[i]
			}
		}
		output += maximal
	}
	return output
}
