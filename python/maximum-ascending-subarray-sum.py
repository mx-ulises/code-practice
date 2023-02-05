class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        maximal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                current = 0
            current += nums[i]
            maximal = max(current, maximal)
        return maximal
