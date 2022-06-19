class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimal, maximal = min(nums), max(nums)
        current = minimal
        while current:
            if maximal % current == 0 and minimal % current == 0:
                return current
            current -= 1
        return -1
