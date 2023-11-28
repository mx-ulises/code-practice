RANGES = [(10, 99), (1000, 9999), (100000, 999999)]

class Solution:
    def has_even_num_of_digits(x: int) -> bool:
        for (start, end) in RANGES:
            if start <= x and x <= end:
                return True
        return False

    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        for x in nums:
            if Solution.has_even_num_of_digits(x):
                output += 1
        return output
