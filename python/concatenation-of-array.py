class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat_count = 2
        output_nums = [0] * (len(nums) * concat_count)
        for i in range(len(nums)):
            for j in range(concat_count):
                output_nums[i + len(nums) * j] = nums[i]
        return output_nums
