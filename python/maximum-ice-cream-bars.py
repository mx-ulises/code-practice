class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        i = 0
        costs.sort()
        while i < len(costs) and costs[i] <= coins:
            coins -= costs[i]
            i += 1
        return i
