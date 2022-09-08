class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        output = []
        minimal = 0
        maximal = len(nums)
        for i in range(maximal):
            if nums[i] == key:
                start = max(minimal, i - k)
                end = min(maximal, i + k + 1)
                for j in range(start, end):
                    output.append(j)
                minimal = end
        return output
