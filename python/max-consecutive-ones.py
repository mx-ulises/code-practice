class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximal_count = 0
        current_count = 0
        for digit in nums:
            if digit:
                current_count += 1
            else:
                current_count = 0
            maximal_count = max(current_count, maximal_count)
        return maximal_count
