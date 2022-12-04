N_MAX = 3

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        h = []
        nums = set(nums)
        for x in nums:
            heappush(h, x)
            if N_MAX < len(h):
                heappop(h)
        output = h[0]
        while h and len(h) != N_MAX:
            output = heappop(h)
        return output
