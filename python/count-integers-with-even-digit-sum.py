class Solution:
    def is_even_digit_sum(x: int) -> bool:
        output = 0
        while x:
            output ^= x
            x //= 10
        return output & 1 == 0

    def countEven(self, num: int) -> int:
        count = 0
        for x in range(1, num + 1):
            if Solution.is_even_digit_sum(x):
                count += 1
        return count
