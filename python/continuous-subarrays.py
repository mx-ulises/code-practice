class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        subarray_count = 1
        start, end = 0, 1
        maximal, minimal = nums[0], nums[0]
        nums_in_subarray = defaultdict(lambda: 0)
        nums_in_subarray[nums[0]] += 1
        while end < len(nums):
            nums_in_subarray[nums[end]] += 1
            maximal = max(maximal, nums[end])
            minimal = min(minimal, nums[end])
            while 2 < (maximal - minimal):
                nums_in_subarray[nums[start]] -= 1
                if nums_in_subarray[nums[start]] == 0:
                    del nums_in_subarray[nums[start]]
                    minimal = min(nums_in_subarray.keys())
                    maximal = max(nums_in_subarray.keys())
                start += 1
            end += 1
            subarray_count += (end - start)
        return subarray_count
