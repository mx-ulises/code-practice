class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1, n + 1):
            if (n % i) == 0:
                j = i - 1
                total += (nums[j] * nums[j])
        return total
