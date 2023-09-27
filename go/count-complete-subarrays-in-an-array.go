func CountDistinctElements(nums []int) int {
	numCount := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		numCount[nums[i]] = true
	}
	return len(numCount)
}

func Solution1(nums []int) int {
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

func Solution2(nums []int) int {
	distinctElements := CountDistinctElements(nums)
	n := len(nums)
	completeSubarrays := 0
	start, end := 0, 0
	numCount := make(map[int]int)
	for end < n {
		numEnd := nums[end]
		numCount[numEnd] += 1
		for len(numCount) == distinctElements {
			numStart := nums[start]
			completeSubarrays += n - end
			numCount[numStart] -= 1
			if numCount[numStart] == 0 {
				delete(numCount, numStart)
			}
			start += 1
		}
		end += 1
	}
	return completeSubarrays
}

func countCompleteSubarrays(nums []int) int {
	return Solution2(nums)
}
