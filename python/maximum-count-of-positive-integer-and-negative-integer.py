class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = bisect_left(nums, 0)
        positives = len(nums) - bisect_right(nums, 0)
        return max(negatives, positives)
