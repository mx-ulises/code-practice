class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.sort()
        else:
            minimal = i
            for j in range(i, len(nums)):
                if nums[i - 1] < nums[j] and nums[j] <= nums[minimal] and minimal < j:
                    minimal = j
            aux = nums[i - 1]
            nums[i - 1] = nums[minimal]
            nums[minimal] = aux
            n = len(nums) - i
            for j in range(n // 2):
                k = j + i
                l = len(nums) - j - 1
                aux = nums[k]
                nums[k] = nums[l]
                nums[l] = aux
