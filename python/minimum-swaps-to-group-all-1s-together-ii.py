class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window_size = sum(nums)
        need_shift = window_size - sum(nums[0:window_size])
        min_swaps = need_shift
        for i in range(n - 1):
            j = (i + window_size) % n
            need_shift += nums[i]
            need_shift -= nums[j]
            min_swaps = min(min_swaps, need_shift)
        return min_swaps
