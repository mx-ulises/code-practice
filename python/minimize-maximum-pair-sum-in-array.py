class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        min_pair_sum = 0
        nums.sort()
        for i in range(len(nums) // 2):
            j = len(nums) - i - 1
            min_pair_sum = max(min_pair_sum, nums[i] + nums[j])
        return min_pair_sum
