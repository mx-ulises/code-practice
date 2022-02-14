class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = min(k + 1, len(nums))
        nums_count = defaultdict(lambda: 0)
        for i in range(len(nums)):
            if k <= i:
                nums_count[nums[i - k]] -= 1
            if nums_count[nums[i]]:
                return True
            nums_count[nums[i]] += 1
        return False
