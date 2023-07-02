func diagonalSum(mat [][]int) int {
	n := len(mat)
	total := 0
	for i := 0; i < n; i++ {
		total += mat[i][i] + mat[i][n-i-1]
	}
	if n&1 == 1 {
		n = n >> 1
		total -= mat[n][n]
	}
	return total
}
