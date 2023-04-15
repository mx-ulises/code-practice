class Solution:
    def minimumSum(self, num: int) -> int:
        h = []
        while num:
            heappush(h, num % 10)
            num //= 10
        result = 0
        while h:
            result *= 10
            result += heappop(h) + heappop(h)
        return result
