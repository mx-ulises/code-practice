class Solution:
    def get_cummulative_arrays(nums: List[int]) -> List[List[int]]:
        cummulative = []
        for i in range(3):
            cummulative.append([0])
            for x in nums:
                cummulative[-1].append(cummulative[-1][-1])
                if x != (i + 1):
                    cummulative[-1][-1] += 1
        return cummulative

    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        minimum_operations = n
        cummulative = Solution.get_cummulative_arrays(nums)
        for i in range(n + 1):
            for j in range(i, n + 1):
                changes_1 = cummulative[0][i]
                changes_2 = cummulative[1][j] - cummulative[1][i]
                changes_3 = cummulative[2][n] - cummulative[2][j]
                candidate = changes_1 + changes_2 + changes_3
                if candidate < minimum_operations:
                    minimum_operations = candidate
        return minimum_operations
