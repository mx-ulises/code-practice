class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarray_count = 0
        subarray_size = 0
        for num in nums:
            if num == 0:
                subarray_size += 1
            else:
                subarray_size = 0
            subarray_count += subarray_size
        return subarray_count
