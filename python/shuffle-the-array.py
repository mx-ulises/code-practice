class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i*2] += (nums[i] % 10000) * 10000
            nums[i*2 + 1] += (nums[n + i] % 10000) * 10000
        for i in range(n):
            nums[i] = int(nums[i]/10000)
            nums[n + i] = int(nums[n + i]/10000)
        return nums
