func maxSatisfaction(satisfaction []int) int {
	sort.Ints(satisfaction)
	currentSum := 0
	currentSatisfaction := 0
	maximalSatisfactiom := 0
	for i := len(satisfaction) - 1; 0 <= i; i-- {
		currentSum += satisfaction[i]
		currentSatisfaction += currentSum
		if maximalSatisfactiom < currentSatisfaction {
			maximalSatisfactiom = currentSatisfaction
		}
	}
	return maximalSatisfactiom
}
