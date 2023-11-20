class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            s = set([nums[i]])
            total += 1
            for j in range(i + 1, len(nums)):
                s.add(nums[j])
                total += len(s) ** 2
        return total
