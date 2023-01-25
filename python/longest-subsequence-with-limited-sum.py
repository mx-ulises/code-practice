class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()
        nums.sort()
        output = [-1] * len(queries)
        total = sum(nums)
        while queries:
            q, i = queries.pop()
            while q < total:
                total -= nums.pop()
            output[i] = len(nums)
        return output
