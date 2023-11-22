class Solution:
    def get_direction(x: int, y: int) -> int:
        if x < y:
            return 1
        if y < x:
            return -1
        return 0
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        direction = 0
        for i in range(1, len(nums)):
            current_direction = Solution.get_direction(nums[i - 1], nums[i])
            if direction == 0:
                direction = current_direction
            if current_direction != 0 and current_direction != direction:
                return False
        return True
