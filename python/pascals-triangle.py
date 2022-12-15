class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        while len(rows) < numRows:
            new_row = [0]
            for i in range(len(rows[-1])):
                new_row[i] += rows[-1][i]
                new_row.append(rows[-1][i])
            rows.append(new_row)
        return rows
