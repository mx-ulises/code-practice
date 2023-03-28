class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_quares = []
        left = 0
        left_square = nums[left] * nums[left]
        right = len(nums) - 1
        right_square = nums[right] * nums[right]
        while left < right:
            if left_square < right_square:
                sorted_quares.append(right_square)
                right -= 1
                right_square = nums[right] * nums[right]
            else:
                sorted_quares.append(left_square)
                left += 1
                left_square = nums[left] * nums[left]
        sorted_quares.append(left_square)
        sorted_quares.reverse()
        return sorted_quares
