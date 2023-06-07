func createTargetArray(nums []int, index []int) []int {
    targetArray := make([]int, 0)
    for i := 0; i < len(nums); i++ {
        newTargetArray := make([]int, len(targetArray) + 1)
        copy(newTargetArray[:index[i]], targetArray[:index[i]])
        newTargetArray[index[i]] = nums[i]
        copy(newTargetArray[index[i] + 1:], targetArray[index[i]:])
        targetArray = newTargetArray
    }
    return targetArray
}
