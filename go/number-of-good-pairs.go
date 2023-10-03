func numIdenticalPairs(nums []int) int {
	goodPairCount := 0
	numCount := make(map[int]int)
	for _, x := range nums {
		goodPairCount += numCount[x]
		numCount[x] += 1
	}
	return goodPairCount
}
