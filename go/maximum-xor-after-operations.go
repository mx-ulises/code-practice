func maximumXOR(nums []int) int {
	maximum := 0
	for i := 0; i < len(nums); i++ {
		maximum |= nums[i]
	}
	return maximum
}
