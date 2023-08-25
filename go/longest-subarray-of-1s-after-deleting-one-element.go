func longestSubarray(nums []int) int {
	prevSegmentSize := 0
	currentSegmentSize := 0
	longestSize := 0
	isThereZeros := false
	for _, num := range nums {
		if num == 1 {
			currentSegmentSize += 1
		} else {
			candidateSize := prevSegmentSize + currentSegmentSize
			if longestSize < candidateSize {
				longestSize = candidateSize
			}
			prevSegmentSize = currentSegmentSize
			currentSegmentSize = 0
			isThereZeros = true
		}
	}
	candidateSize := prevSegmentSize + currentSegmentSize
	if longestSize < candidateSize {
		longestSize = candidateSize
	}
	if isThereZeros == false {
		longestSize -= 1
	}
	return longestSize
}
