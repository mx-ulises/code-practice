func CountDistinctElements(nums []int) int {
	numCount := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		numCount[nums[i]] = true
	}
	return len(numCount)
}

func countCompleteSubarrays(nums []int) int {
	distinctElements := CountDistinctElements(nums)
	completeSubarrays := 0
	n := len(nums)
	for i := 0; i < n; i++ {
		numCount := make(map[int]bool)
		for j := i; j < n; j++ {
			numCount[nums[j]] = true
			if len(numCount) == distinctElements {
				completeSubarrays += n - j
				break
			}
		}
	}
	return completeSubarrays
}
