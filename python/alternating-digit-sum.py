class Solution:
    def alternateDigitSum(self, n: int) -> int:
        alternative_sum = 0
        digit_count = 0
        while n:
            digit_count ^= 1
            if digit_count & 1:
                alternative_sum += n % 10
            else:
                alternative_sum -= n % 10
            n = n // 10
        if digit_count & 1 == 0:
            alternative_sum = -alternative_sum
        return alternative_sum
