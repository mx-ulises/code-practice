class Solution:
    def totalMoney(self, n: int) -> int:
        start_ammount = 1
        total = 0
        while 7 <= n:
            total += 21 + 7 * start_ammount
            start_ammount += 1
            n -= 7
        while n:
            total += start_ammount
            start_ammount += 1
            n -= 1
        return total
