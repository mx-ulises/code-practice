func findPrefixScore(nums []int) []int64 {
	answer := make([]int64, 0)
	score := int64(0)
	maximal := int64(0)
	for _, num := range nums {
		num := int64(num)
		if maximal < num {
			maximal = num
		}
		score += num + maximal
		answer = append(answer, score)
	}
	return answer
}
