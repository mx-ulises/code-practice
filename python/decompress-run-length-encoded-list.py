class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums) // 2):
            f, v = nums[i * 2], nums[i * 2 + 1]
            output += [v] * f
        return output
