class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        out = 0
        for i in range(len(tickets)):
            if i <= k:
                out += min(tickets[k], tickets[i])
            else:
                out += min(tickets[k] - 1, tickets[i])
        return out
