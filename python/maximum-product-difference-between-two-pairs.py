class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        h = []
        for i in range(4):
            heappush(h, nums[i])
        d = heappop(h)
        c = heappop(h)
        for i in range(4, len(nums)):
            heappush(h, nums[i])
            x = heappop(h)
            if x < d:
                c = d
                d = x
            elif x < c:
                c = x
        b = heappop(h)
        a = heappop(h)
        return (a * b) - (c * d)
