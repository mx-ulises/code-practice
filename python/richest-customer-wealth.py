class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximal = 0
        for customer in accounts:
            maximal = max(maximal, sum(customer))
        return maximal
