func zeroFilledSubarray(nums []int) int64 {
	subarraySize := int64(0)
	subarrayCount := int64(0)
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			subarraySize += 1
		} else {
			subarraySize = 0
		}
		subarrayCount += subarraySize
	}
	return subarrayCount
}
