from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        summatory = [nums[0]]
        maximal = max(nums)
        minimal = deque([(0, min(0, summatory[-1]))])
        for i in range(1, len(nums) * 2):
            #print("{}, {}".format(minimal, maximal))
            j = i % len(nums)
            summatory.append(summatory[-1] + nums[j])
            if minimal[0][0] <= (i - len(nums)):
                minimal.popleft()
            maximal = max(maximal, summatory[-1] - minimal[0][1])
            while minimal and summatory[-1] < minimal[-1][1]:
                minimal.pop()
            minimal.append((i, summatory[-1]))
        return maximal
