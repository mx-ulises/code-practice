class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs_on = 0
        i = 1
        while (i * i) <= n:
            bulbs_on += 1
            i += 1
        return bulbs_on
