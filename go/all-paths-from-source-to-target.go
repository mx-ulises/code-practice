func getPaths(graph *[][]int, current_path *[]int, solutions *[][]int, target int) {
    current_path_size := len(*current_path)
    tail := (*current_path)[current_path_size - 1]
    if tail == target {
        solution := make([]int, current_path_size)
        copy(solution, *current_path)
        *solutions = append(*solutions, solution)
    } else {
        for i := 0; i < len((*graph)[tail]); i++ {
            new_tail := (*graph)[tail][i]
            *current_path = append(*current_path, new_tail)
            getPaths(graph, current_path, solutions, target)
            *current_path = (*current_path)[:current_path_size]
        }
    }
}

func allPathsSourceTarget(graph [][]int) [][]int {
    var solutions [][]int
    current_path := make([]int, 1)
    target := len(graph) - 1
    getPaths(&graph, &current_path, &solutions, target)
    return solutions
}
