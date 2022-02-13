class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        current_sum = 1
        left, right = 2, int(num / 2)
        while left <= right:
            if num % left == 0:
                current_sum += left
                if left != right:
                    current_sum += right
                if current_sum > num:
                    return False
            left += 1
            right = int(num / left)
        return current_sum == num
