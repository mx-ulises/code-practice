class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        previous = defaultdict(lambda: 0)
        pair_count = 0
        for num in nums:
            pair_count += previous[num - k]
            pair_count += previous[num + k]
            previous[num] += 1
        return pair_count
