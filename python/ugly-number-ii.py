class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        latest = 1
        visited = set()
        while n:
            latest = heappop(h)
            for p in [2, 3, 5]:
                x = p * latest
                if x not in visited:
                    heappush(h, x)
                visited.add(x)
            n -= 1
        return latest
