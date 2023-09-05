class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        a = max(nums) * k
        b = k * (k - 1) // 2
        return a + b
