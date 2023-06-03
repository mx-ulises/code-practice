import (
    "math"
)

func getMaximumXor(nums []int, maximumBit int) []int {
    answer := make([]int, 0)
    current := int(math.Pow(2, float64(maximumBit))) - 1;
    for i := 0; i < len(nums); i++ {
        current ^= nums[i]
    }
    for i := 0; i < len(nums); i++ {
        answer = append(answer, current)
        current ^= nums[len(nums) - i - 1]
    }
    return answer
}
