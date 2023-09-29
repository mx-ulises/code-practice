func minimumSum(n int, k int) int {
	output := 0
	current := 0
	firstLimit := (k / 2) + 1
	if (n + 1) < firstLimit {
		firstLimit = n + 1
	}
	for current < firstLimit {
		output += current
		current += 1
	}
	secondLimit := k + n - current
	current = k
	for current <= secondLimit {
		output += current
		current += 1
	}
	return output
}
