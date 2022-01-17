class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(lambda: 0)
        for a in arr:
            count[a] += 1
        max_lucky = -1
        for a in count:
            if a == count[a]:
                max_lucky = max(a, max_lucky)
        return max_lucky
