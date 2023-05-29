func findThePrefixCommonArray(A []int, B []int) []int {
    A_set := make([]bool, len(A))
    B_set := make([]bool, len(A))
    C := make([]int, len(A))
    common := 0
    for i := 0; i < len(A); i++ {
        a := A[i] - 1
        b := B[i] - 1
        A_set[a] = true
        B_set[b] = true
        if B_set[a] {
            common += 1
        }
        if A_set[b] {
            common += 1
        }
        if a == b {
            common -= 1
        }
        C[i] = common
    }
    return C
}
