class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(list)
        while nums:
            i = len(nums) - 1
            nums_map[nums.pop()].append(i)
        pairs = 0
        for x in nums_map:
            while nums_map[x]:
                i = nums_map[x].pop()
                for j in nums_map[x]:
                    if (i * j) % k == 0:
                        pairs += 1
        return pairs
