func triangularSum(nums []int) int {
    for tail := len(nums); 1 < tail; tail-- {
        for i := 1; i < tail; i++ {
            nums[i - 1] += nums[i]
            nums[i - 1] %= 10
        }
    }
    return nums[0]
}
