class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = [0] * len(nums)
        for x in nums:
            s[x - 1] += 1
        repeated, missing = 0, 0
        for i in range(len(s)):
            if s[i] == 0:
                missing = i + 1
            elif s[i] == 2:
                repeated = i + 1
        return [repeated, missing]
