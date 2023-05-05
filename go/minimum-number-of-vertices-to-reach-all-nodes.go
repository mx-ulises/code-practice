func findSmallestSetOfVertices(n int, edges [][]int) []int {
    visitedVertices := make(map[int]bool)
    for i := 0; i < len(edges); i++ {
        visitedVertices[edges[i][1]] = true;
    }
    smallestSetOfVertices := []int{}
    for i := 0; i < n; i++ {
        visited, ok := visitedVertices[i]
        if ok == false || visited != true {
            smallestSetOfVertices = append(smallestSetOfVertices, i)
        }
    }
    return smallestSetOfVertices
}
