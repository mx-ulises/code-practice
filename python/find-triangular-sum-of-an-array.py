class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        tail = len(nums)
        while tail != 1:
            for i in range(1, tail):
                nums[i - 1] += nums[i]
            tail -= 1
        return nums[0] % 10
