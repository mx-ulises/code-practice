func GetGridSum(grid [][]int, x int, y int) int {
    gridSum := grid[x][y] + grid[x][y + 1] + grid[x][y + 2]
    gridSum += grid[x + 1][y + 1]
    gridSum += grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]
    return gridSum
}

func maxSum(grid [][]int) int {
    currentMaxSum := 0
    for i := 0; i < (len(grid) - 2); i++ {
        for j := 0; j < (len(grid[i]) - 2); j++ {
            candidateMaxSum := GetGridSum(grid, i, j)
            if currentMaxSum < candidateMaxSum {
                currentMaxSum = candidateMaxSum;
            }
        }
    }
    return currentMaxSum
}
