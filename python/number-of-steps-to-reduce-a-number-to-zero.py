class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while 1 < num:
            steps += 1 + (num & 1)
            num >>= 1
        return steps + num
