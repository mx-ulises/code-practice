class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        last_line = 0
        offset = ord('a')
        for c in s:
            i = ord(c) - offset
            if 100 < (last_line + widths[i]):
                last_line = widths[i]
                lines += 1
            else:
                last_line += widths[i]
        return [lines, last_line]
