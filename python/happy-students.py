class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ways = 0
        if 0 < nums[0]:
            ways += 1
        for i in range(1, len(nums)):
            if i < nums[i] and nums[i - 1] < i:
                ways += 1
        if nums[-1] < len(nums):
            ways += 1
        return ways
