import (
    "sort"
)

func minPairSum(nums []int) int {
    minPair := 0
    sort.Ints(nums)
    for i := 0; i < len(nums) / 2; i++ {
        candidate := nums[i] + nums[len(nums) - i - 1]
        if minPair < candidate {
            minPair = candidate
        }
    }
    return minPair
}
