class Solution:
    def maximum69Number (self, num: int) -> int:
        maximal = num
        mask = 1
        while num // mask:
            digit = (num % (mask * 10)) // mask
            if digit == 6:
                candidate = num + (3 * mask)
                maximal = max(maximal, candidate)
            mask *= 10
        return maximal
