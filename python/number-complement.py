class Solution:
    def solution_1(num: int) -> int:
        power = 0
        n = num
        while n:
            power += 1
            n = n >> 1
        return ((2 ** power)  - 1) ^ num

    def solution_2(num: int) -> int:
        power = int(math.log(num, 2)) + 1
        return ((2 ** power)  - 1) ^ num

    def findComplement(self, num: int) -> int:
        return Solution.solution_1(num)
