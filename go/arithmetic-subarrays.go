func IsArithmeticSubarray(subarray []int) bool {
	if len(subarray) < 2 {
		return false
	}
	sort.Ints(subarray)
	diff := subarray[1] - subarray[0]
	for i := 1; i < len(subarray); i++ {
		if (subarray[i] - subarray[i-1]) != diff {
			return false
		}
	}
	return true
}

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	output := make([]bool, 0)
	for i := 0; i < len(l); i++ {
		start := l[i]
		end := r[i] + 1
		subarray := make([]int, end-start)
		copy(subarray, nums[start:end])
		output = append(output, IsArithmeticSubarray(subarray))
	}
	return output
}
