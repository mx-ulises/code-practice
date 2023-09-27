class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        complete_subarrays = 0
        n = len(nums)
        for i in range(n):
            current_nums = set()
            for j in range(i, n):
                current_nums.add(nums[j])
                if len(current_nums) == distinct_count:
                    complete_subarrays += n - j
                    break
        return complete_subarrays
