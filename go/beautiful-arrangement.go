func validPosition(i int, perm_i int, perm []bool) bool {
    if perm[i] {
        return false
    }
    return (i % perm_i) == 0 || (perm_i % i) == 0
}

func countBeautifulArrangement(perm_i int, perm []bool) int {
    if perm_i == len(perm) {
        return 1
    }
    count := 0
    for i := 1; i < len(perm); i++ {
        if validPosition(i, perm_i, perm) {
            perm[i] = true
            count += countBeautifulArrangement(perm_i + 1, perm)
            perm[i] = false
        }
    }
    return count
}

func countArrangement(n int) int {
    perm := make([]bool, n + 1)
    return countBeautifulArrangement(1, perm)
}
