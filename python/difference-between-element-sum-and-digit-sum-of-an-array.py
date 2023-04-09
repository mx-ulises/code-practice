class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        diff = 0
        for x in nums:
            diff += x
            while x:
                diff -= x % 10
                x //= 10
        return diff
