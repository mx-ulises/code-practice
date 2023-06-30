func findDuplicates(nums []int) []int {
	dupes := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		for nums[i] != 0 && (i+1) != nums[i] && nums[i] != nums[nums[i]-1] {
			aux := nums[i]
			nums[i] = nums[nums[i]-1]
			nums[aux-1] = aux
		}
		if nums[i] != 0 && nums[i] == nums[nums[i]-1] && (i+1) != nums[i] {
			dupes = append(dupes, nums[i])
			nums[i] = 0
		}
	}
	return dupes
}
