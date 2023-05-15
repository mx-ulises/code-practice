func countVowelStrings(n int) int {
    vowels_count := 5
    endWith := [5]int {1, 1, 1, 1, 1}
    var currentCount int
    for i := 0; i < n; i++ {
        currentCount = 0
        for j := 0; j < vowels_count; j++ {
            currentCount += endWith[j]
            endWith[j] = currentCount
        }
    }
    return currentCount
}
