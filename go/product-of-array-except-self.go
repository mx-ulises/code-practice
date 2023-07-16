func productExceptSelf(nums []int) []int {
	n := len(nums)
	output := make([]int, n)
	last := n - 1
	output[last] = nums[last]
	for i := 0; i < last; i++ {
		j := n - i - 1
		prev := j - 1
		output[prev] = output[j] * nums[prev]
	}
	cummulative := 1
	for i := 0; i < last; i++ {
		output[i] = cummulative * output[i+1]
		cummulative *= nums[i]
	}
	output[last] = cummulative
	return output
}
