func minFlips(target string) int {
	current := '0'
	count := 0
	for _, b := range target {
		if current != b {
			current = b
			count += 1
		}
	}
	return count
}
