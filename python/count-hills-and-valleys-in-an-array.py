class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        direction = 0
        count = 0
        i = 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1
        while i < len(nums):
            if nums[i - 1] < nums[i] and direction != 1:
                count += 1
                direction = 1
            elif nums[i] < nums[i - 1] and direction != -1:
                count += 1
                direction = -1
            i += 1
        return max(0, count - 1)
