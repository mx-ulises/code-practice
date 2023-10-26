class Solution:
    def is_valid(num: int) -> bool:
        return num % 3 == 0 and num % 2 == 0

    def averageValue(self, nums: List[int]) -> int:
        total, count = 0, 0
        for num in nums:
            if Solution.is_valid(num):
                total += num
                count += 1
        if count == 0:
            return 0
        return total // count
