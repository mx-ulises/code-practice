class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        differences = []
        for x in nums:
            right -= x
            diff = abs(right - left)
            differences.append(diff)
            left += x
        return differences
