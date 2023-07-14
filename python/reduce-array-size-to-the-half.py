class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        int_count = defaultdict(lambda: 0)
        for x in arr:
            int_count[x] += 1
        counts = [int_count[x] for x in int_count]
        counts.sort()
        set_size = 0
        n = len(arr)
        while (len(arr) // 2) < n:
            n -= counts.pop()
            set_size += 1
        return set_size
