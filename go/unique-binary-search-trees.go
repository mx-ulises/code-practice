func numTrees(n int) int {
	trees := make([]int, 2)
	trees[0] = 1
	trees[1] = 1
	for total_nodes := 2; total_nodes < (n + 1); total_nodes++ {
		trees = append(trees, 0)
		for left_nodes := 0; left_nodes < total_nodes; left_nodes++ {
			right_nodes := total_nodes - left_nodes - 1
			trees[total_nodes] += trees[left_nodes] * trees[right_nodes]
		}
	}
	return trees[n]
}
