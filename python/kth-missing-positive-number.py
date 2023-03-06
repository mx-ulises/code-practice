class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for x in arr:
            delta = x - prev - 1
            if k <= delta:
                break
            k -= delta
            prev = x
        return prev + k
