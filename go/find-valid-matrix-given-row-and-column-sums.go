func restoreMatrix(rowSum []int, colSum []int) [][]int {
	n, m := len(rowSum), len(colSum)
	outputMatrix := make([][]int, n)
	for i := 0; i < n; i++ {
		outputMatrix[i] = make([]int, m)
	}
	startColIndex := 0
	for i := 0; i < n; i++ {
		for j := startColIndex; j < m; j++ {
			minimalSubstraction := rowSum[i]
			if colSum[j] < minimalSubstraction {
				minimalSubstraction = colSum[j]
			}
			rowSum[i] -= minimalSubstraction
			colSum[j] -= minimalSubstraction
			outputMatrix[i][j] = minimalSubstraction
			if colSum[j] == 0 {
				startColIndex = j
			}
			if rowSum[i] == 0 {
				break
			}
		}
	}
	return outputMatrix
}
