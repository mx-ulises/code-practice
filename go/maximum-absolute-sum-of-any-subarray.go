func maxAbsoluteSum(nums []int) int {
	currentSum := 0
	minimal := 0
	maximal := 0
	for i := 0; i < len(nums); i++ {
		currentSum += nums[i]
		if maximal < currentSum {
			maximal = currentSum
		}
		if currentSum < minimal {
			minimal = currentSum
		}
	}
	difference := maximal - minimal
	if difference < 0 {
		difference = -difference
	}
	return difference
}
