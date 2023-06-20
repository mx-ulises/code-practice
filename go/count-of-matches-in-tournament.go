func algorithmSolution(n int) int {
	matchCount := 0
	for 1 < n {
		isOdd := n & 1
		matchInRound := n / 2
		matchCount += matchInRound
		n = matchInRound + isOdd
	}
	return matchCount
}

func numberOfMatches(n int) int {
	//return algorithmSolution(n)
	return n - 1
}
