class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minimal = min(nums) + k
        maximal = max(nums) - k
        return max(0, maximal - minimal)
