class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sums = [0]
        visited = {}
        maximum_score = 0
        start = 0
        for i in range(len(nums)):
            num = nums[i]
            sums.append(sums[-1] + nums[i])
            if num in visited:
                start = max(start, visited[num] + 1)
            maximum_score = max(maximum_score, sums[i + 1] - sums[start])
            visited[num] = i
        maximum_score = max(maximum_score, sums[i + 1] - sums[start])
        return maximum_score
