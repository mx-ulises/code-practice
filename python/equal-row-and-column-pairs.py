class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(lambda: 0)
        columns = defaultdict(lambda: 0)
        for i in range(len(grid)):
            row = "_".join(map(str, grid[i]))
            rows[row] += 1
            column = "_".join([str(elements[i]) for elements in grid])
            columns[column] += 1
        pairs = 0
        for row in rows:
            pairs += rows[row] * columns[row]
        return pairs
