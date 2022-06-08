class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        col_number = 0
        m = 1
        for i in range(n):
            c = columnTitle[n - i - 1]
            c_ord = ord(c) - ord('A') + 1
            col_number += c_ord * m
            m *= 26
        return col_number
