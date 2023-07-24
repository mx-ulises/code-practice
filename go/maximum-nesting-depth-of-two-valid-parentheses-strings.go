func maxDepthAfterSplit(seq string) []int {
	output := make([]int, 0)
	current := 0
	maximal := 0
	for i := 0; i < len(seq); i++ {
		if seq[i] == '(' {
			output = append(output, current)
			current += 1
			if maximal < current {
				maximal = current
			}
		} else {
			current -= 1
			output = append(output, current)
		}
	}
	mean := maximal / 2
	for i := 0; i < len(output); i++ {
		if output[i] < mean {
			output[i] = 1
		} else {
			output[i] = 0
		}
	}
	return output
}
