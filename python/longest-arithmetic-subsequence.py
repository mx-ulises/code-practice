class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = nums[0] - nums[1]
        diff_map = {(d, 1): 2}
        maximal = 2
        for i in range(2, len(nums)):
            for j in range(i):
                d = nums[j] - nums[i]
                if (d, j) in diff_map:
                    diff_map[(d, i)] = diff_map[(d, j)] + 1
                    maximal = max(maximal, diff_map[(d, i)])
                else:
                    diff_map[(d, i)] = 2
        return maximal
