class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_values = [nums[i] for i in range(len(nums)) if i % 2 == 1]
        even_values = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        even_values.sort()
        odd_values.sort()
        odd_values.reverse()
        i = 0
        while even_values and odd_values:
            nums[i] = even_values.pop(0)
            nums[i + 1] = odd_values.pop(0)
            i += 2
        if even_values:
            nums[i] = even_values.pop(0)
        return nums
