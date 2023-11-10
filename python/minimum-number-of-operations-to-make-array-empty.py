class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        num_count = defaultdict(lambda: 0)
        while nums:
            num_count[nums.pop()] += 1
        for x in num_count:
            count = num_count[x]
            if count == 1:
                return -1
            operations += count // 3
            if (count % 3) != 0:
                operations += 1
        return operations
