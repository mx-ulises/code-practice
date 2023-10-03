class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = defaultdict(lambda: 0)
        for x in arr:
            num_count[x] += 1
        occurrences = set([num_count[x] for x in num_count])
        return len(num_count) == len(occurrences)
