class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimal = 100000
        max_profit = 0
        for price in prices:
            if price < minimal:
                minimal = price
            max_profit = max(max_profit, price - minimal)
        return max_profit
