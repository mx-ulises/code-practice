class Solution:
    def get_min_max(nums, start, end, OPERATION):
        if start == end:
            return nums[start]
        mid = (start + end) // 2
        left = Solution.get_min_max(nums, start, mid, min)
        right = Solution.get_min_max(nums, mid + 1, end, max)
        return OPERATION(left, right)

    def minMaxGame(self, nums: List[int]) -> int:
        return Solution.get_min_max(nums, 0, len(nums) - 1, min)
