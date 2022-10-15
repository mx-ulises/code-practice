class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            complete_row_coins = mid * (mid + 1) / 2
            if n == complete_row_coins:
                return mid
            if n < complete_row_coins:
                right = mid - 1
            else:
                left = mid + 1
        return right
