class Solution:
    def countDigits(self, num: int) -> int:
        digit_count = 0
        num_aux = num
        while num_aux:
            digit = num_aux % 10
            num_aux //= 10
            if (num % digit) == 0:
                digit_count += 1
        return digit_count
