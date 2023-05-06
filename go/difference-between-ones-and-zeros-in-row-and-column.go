func onesMinusZeros(grid [][]int) [][]int {
    n, m := len(grid), len(grid[0])
    ones_row := make([]int, n)
    ones_col := make([]int, m)
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            is_one := grid[i][j]
            ones_row[i] += is_one
            ones_col[j] += is_one
        }
    }
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            grid[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - n - m
        }
    }
    return grid
}
