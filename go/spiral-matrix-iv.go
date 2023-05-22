/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func InitMatrix(m int, n int) [][]int {
    spiralMatrixOutput := make([][]int, m)
    for i := range spiralMatrixOutput {
        spiralMatrixOutput[i] = make([]int, n)
        for j := range spiralMatrixOutput[i] {
            spiralMatrixOutput[i][j] = -1
        }
    }
    return spiralMatrixOutput
}

func IsInRange(i int, m int) bool {
    return 0 <= i && i < m
}

func GetDirectionIndex(i int, j int, m int, n int, directionIndex int, spiralMatrixOutput [][]int, directions [][]int) int {
    direction := directions[directionIndex]
    i += direction[0]
    j += direction[1]
    if !IsInRange(i, m) || !IsInRange(j, n) || spiralMatrixOutput[i][j] != -1 {
        directionIndex = (directionIndex + 1) % 4
    }
    return directionIndex
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    directions := [][]int{
        {0, 1},
        {1, 0},
        {0, -1},
        {-1, 0},
    }
    spiralMatrixOutput := InitMatrix(m, n)
    i, j, directionIndex := 0, 0, 0
    for head != nil {
        spiralMatrixOutput[i][j] = head.Val
        directionIndex = GetDirectionIndex(i, j, m, n, directionIndex, spiralMatrixOutput, directions)
        direction := directions[directionIndex]
        i += direction[0]
        j += direction[1]
        head = head.Next
    }
    return spiralMatrixOutput
}
