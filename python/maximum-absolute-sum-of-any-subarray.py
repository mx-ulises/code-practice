class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_sum = 0
        minimal = 0
        maximal = 0
        for num in nums:
            current_sum += num
            minimal = min(minimal, current_sum)
            maximal = max(maximal, current_sum)
        return abs(maximal - minimal)
