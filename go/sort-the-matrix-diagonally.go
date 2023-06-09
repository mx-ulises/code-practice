import (
    "sort"
)

func get_diagonal(mat [][]int, x int, y int) []int {
    diagonal := make([]int, 0)
    for x < len(mat) && y < len(mat[x]) {
        diagonal = append(diagonal, mat[x][y])
        x += 1
        y += 1
    }
    return diagonal
}

func fill_diagonal(mat [][]int, x int, y int, diagonal []int) {
    for i := 0; i < len(diagonal); i++ {
        mat[x + i][y + i] = diagonal[i]
    }
}

func sort_diagonal(mat [][]int, x int, y int) {
    diagonal := get_diagonal(mat, x, y)
    sort.Ints(diagonal)
    fill_diagonal(mat, x, y, diagonal)
}

func diagonalSort(mat [][]int) [][]int {
    for x := 0; x < len(mat); x++ {
        sort_diagonal(mat, x, 0)
    }
    for y := 1; y < len(mat[0]); y++ {
        sort_diagonal(mat, 0, y)
    }
    return mat
}
