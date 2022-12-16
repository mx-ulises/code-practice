class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            new_row = [0]
            for j in range(i + 1):
                new_row[j] += row[j]
                new_row.append(row[j])
            row = new_row
        return row
