func countKDifference(nums []int, k int) int {
	previous := make(map[int]int)
	count := 0
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		count += previous[num-k]
		count += previous[num+k]
		previous[num] += 1
	}
	return count
}
