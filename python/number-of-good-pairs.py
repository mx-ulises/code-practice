class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair_count = 0
        num_count = defaultdict(lambda: 0)
        for x in nums:
            good_pair_count += num_count[x]
            num_count[x] += 1
        return good_pair_count
