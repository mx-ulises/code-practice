class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 0:
                i += 1
            while i < j and nums[j] & 1 == 1:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
