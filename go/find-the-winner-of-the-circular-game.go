func SubOptimalSolution(n int, k int) int {
    if k == 1 {
        return n
    }
    graph := make([]int, n + 1)
    for i := 0; i < n; i++ {
        graph[i] = i + 1
    }
    graph[n] = 1
    current_friend := 0
    for graph[current_friend] != current_friend {
        for i := 0; i < (k - 1); i++ {
            current_friend = graph[current_friend]
        }
        next_friend := graph[current_friend]
        graph[current_friend] = graph[next_friend]
    }
    return current_friend
}

func OptimalSolution(n int, k int) int {
    pos := 0
    for i := 2; i < n + 1; i++ {
        pos = (pos + k) % i
    }
    return pos + 1
}

func findTheWinner(n int, k int) int {
    return OptimalSolution(n, k)
}
