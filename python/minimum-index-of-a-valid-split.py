class Solution:
    def get_dominant(nums: List[int]) -> int:
        dominant = 0
        dominant_count = 0
        for num in nums:
            if dominant_count == 0:
                dominant = num
            if num == dominant:
                dominant_count += 1
            else:
                dominant_count -= 1
        return dominant

    def get_dominant_count(nums: List[int], dominant: int) -> int:
        dominant_count = 0
        for num in nums:
            if num == dominant:
                dominant_count += 1
        return dominant_count

    def minimumIndex(self, nums: List[int]) -> int:
        dominant = Solution.get_dominant(nums)
        dominant_pending = Solution.get_dominant_count(nums, dominant) * 2
        dominant_found = 0
        n = len(nums)
        for i in range(n):
            j = n - i
            if i < dominant_found and j < dominant_pending:
                return i - 1
            if nums[i] == dominant:
                dominant_found += 2
                dominant_pending -= 2
        return -1
