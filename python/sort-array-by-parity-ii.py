class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_i, odd_i = 0, 1
        n = len(nums)
        while even_i < n and odd_i < n:
            if nums[even_i] & 1 == 1 and nums[odd_i] & 1 == 0:
                nums[even_i], nums[odd_i] = nums[odd_i], nums[even_i]
            if nums[even_i] & 1 == 0:
                even_i += 2
            if nums[odd_i] & 1 == 1:
                odd_i += 2
        return nums
