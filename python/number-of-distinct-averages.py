class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = set([])
        nums.sort()
        for i in range(len(nums) // 2):
            averages.add((nums[i] + nums[len(nums) - i - 1]) / 2)
        return len(averages)
