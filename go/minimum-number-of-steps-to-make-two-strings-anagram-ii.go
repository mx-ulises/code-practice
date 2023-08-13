func minSteps(s string, t string) int {
	charCount := make([]int, 26)
	for i := 0; i < len(s); i++ {
		c := int(s[i] - 'a')
		charCount[c] += 1
	}
	for i := 0; i < len(t); i++ {
		c := int(t[i] - 'a')
		charCount[c] -= 1
	}
	steps := 0
	for _, v := range charCount {
		if v < 0 {
			v = -v
		}
		steps += v
	}
	return steps
}
