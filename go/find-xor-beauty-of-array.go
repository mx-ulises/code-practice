func xorBeauty(nums []int) int {
	output := 0
	for i := 0; i < len(nums); i++ {
		output ^= nums[i]
	}
	return output
}
