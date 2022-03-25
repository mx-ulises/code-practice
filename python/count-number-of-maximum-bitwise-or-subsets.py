class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s = defaultdict(lambda: 0)
        s[0] = 1
        maximal = 0
        for i in range(len(nums)):
            a = nums[i]
            t = []
            for b in s:
                c = a | b
                t.append((c, s[b]))
                maximal = max(maximal, c)
            for c, count in t:
                s[c] += count
        return s[maximal]
