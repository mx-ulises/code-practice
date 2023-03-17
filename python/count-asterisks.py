class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_open = False
        asterisk_count = 0
        for c in s:
            if c == '|':
                bar_open ^= True
            if c == '*' and not bar_open:
                asterisk_count += 1
        return asterisk_count
