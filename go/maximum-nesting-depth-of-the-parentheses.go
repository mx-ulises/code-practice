func maxDepth(s string) int {
	currentDepth := 0
	maximalDepth := 0
	for _, c := range s {
		if c == '(' {
			currentDepth += 1
		}
		if c == ')' {
			if maximalDepth < currentDepth {
				maximalDepth = currentDepth
			}
			currentDepth -= 1
		}
	}
	return maximalDepth
}
