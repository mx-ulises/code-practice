import (
    "sort"
)

func maxCoins(piles []int) int {
    left, right := 0, len(piles) - 1
    max_coins := 0
    sort.Ints(piles)
    for left < right {
        max_coins += piles[right -1]
        left += 1
        right -= 2
    }
    return max_coins
}
