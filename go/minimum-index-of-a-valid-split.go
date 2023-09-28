func GetDominant(nums []int) int {
	dominant := 0
	dominantCount := 0
	for _, num := range nums {
		if dominantCount == 0 {
			dominant = num
		}
		if num == dominant {
			dominantCount += 1
		} else {
			dominantCount -= 1
		}
	}
	return dominant
}

func GetNumCount(nums []int, num int) int {
	count := 0
	for _, numInArray := range nums {
		if num == numInArray {
			count += 1
		}
	}
	return count
}

func minimumIndex(nums []int) int {
	dominant := GetDominant(nums)
	dominantPending := 2 * GetNumCount(nums, dominant)
	dominantFound := 0
	for i := 0; i < len(nums); i++ {
		j := len(nums) - i
		if i < dominantFound && j < dominantPending {
			return i - 1
		}
		if nums[i] == dominant {
			dominantPending -= 2
			dominantFound += 2
		}
	}
	return -1
}
