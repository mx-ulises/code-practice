class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        left = 0
        right = len(piles) - 1
        while left < right:
            max_coins += piles[right - 1]
            left += 1
            right -= 2
        return max_coins
