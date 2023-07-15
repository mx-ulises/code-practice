BUY, SELL = 0, 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_price = 10000
        purchase_price = 0
        profit = 0
        next_operation = BUY
        for price in prices:
            if next_operation == BUY and previous_price < price:
                next_operation = SELL
                purchase_price = previous_price
            elif next_operation == SELL and price < previous_price:
                next_operation = BUY
                profit += previous_price - purchase_price
            previous_price = price
        if next_operation == SELL:
            profit += previous_price - purchase_price
        return profit
