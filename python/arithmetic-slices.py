'''
1,2,3,4,5,7,9

[1,2,3,4,5] diff: 1
[5,7,9] diff 2
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        d = nums[0] - nums[1]
        slice_len = 2
        sub_array_count = 0
        for i in range(2, len(nums)):
            new_d = nums[i - 1] - nums[i]
            if new_d == d:
                slice_len += 1
                sub_array_count += slice_len - 2
            else:
                slice_len = 2
            d = new_d
        return sub_array_count
