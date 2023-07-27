class Solution:
    def get_reverse_num(num: int) -> int:
        reverse_num = 0
        while 0 < num:
            reverse_num = (reverse_num * 10) + (num % 10)
            num //= 10
        return reverse_num

    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = set(nums)
        new_nums = set()
        count = len(nums)
        for num in nums:
            reverse_num = Solution.get_reverse_num(num)
            if reverse_num not in nums and reverse_num not in new_nums:
                count += 1
                new_nums.add(reverse_num)
        return count
