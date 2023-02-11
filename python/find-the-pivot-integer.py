class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        sum_left = 1
        sum_right = n
        while left < right:
            if sum_left <= sum_right:
                left += 1
                sum_left += left
            else:
                right -= 1
                sum_right += right
        if sum_left == sum_right:
            return left
        return -1
