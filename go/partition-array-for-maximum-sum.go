func maxSumAfterPartitioning(arr []int, k int) int {
    n := len(arr)
    memory := make([]int, n + 1)
    for i := 0; i < n; i++ {
        current_maximal := arr[i]
        for j := 0; j < k; j++ {
            l := i - j
            if l < 0 {
                break
            }
            if current_maximal < arr[l] {
                current_maximal = arr[l]
            }
            candidate := memory[l] + (current_maximal * (j + 1))
            if memory[i + 1] < candidate {
                memory[i + 1] = candidate
            }
        }
    }
    return memory[n]
}
