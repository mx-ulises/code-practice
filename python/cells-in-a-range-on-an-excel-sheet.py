class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_col, start_row, end_col, end_row = s[0], s[1], s[3], s[4]
        output = []
        for i in range(ord(start_col), ord(end_col) + 1):
            for j in range(ord(start_row), ord(end_row) + 1):
                col, row = chr(i), chr(j)
                cell = f"{col}{row}"
                output.append(cell)
        return output
