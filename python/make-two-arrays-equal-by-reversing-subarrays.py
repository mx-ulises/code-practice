class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        char_count = defaultdict(lambda: 0)
        for c in target:
            char_count[c] += 1
        for c in arr:
            char_count[c] -= 1
            if char_count[c] < 0:
                return False
        return True
