class Solution:
    def solution_2(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        n = len(nums)
        complete_subarrays = 0
        start = 0
        end = 0
        current_subarray = defaultdict(lambda: 0)
        while end < n:
            num_end = nums[end]
            current_subarray[num_end] += 1
            while len(current_subarray) == distinct_count:
                num_start = nums[start]
                complete_subarrays += n - end
                current_subarray[num_start] -= 1
                if current_subarray[num_start] == 0:
                    del current_subarray[num_start]
                start += 1
            end += 1
        return complete_subarrays

    def solution_1(self, nums: List[int]) -> int:
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

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        return self.solution_2(nums)
