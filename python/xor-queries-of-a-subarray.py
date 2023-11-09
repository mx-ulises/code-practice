class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        accumulator = [0]
        for x in arr:
            accumulator.append(accumulator[-1] ^ x)
        output = []
        for query in queries:
            start, end = query[0], query[1] + 1
            output.append(accumulator[start] ^ accumulator[end])
        return output
