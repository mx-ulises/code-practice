class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            a, b = min(num1, num2), max(num1, num2)
            count += b // a
            num1 = b % a
            num2 = a
        return count
