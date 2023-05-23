class Solution:
    def grayCode(self, n: int) -> List[int]:
        visited = set([0])
        moves = [2 ** i for i in range(n)]
        output = []
        s = [0]
        while s:
            x = s.pop()
            output.append(x)
            for move in moves:
                y = x ^ move
                if y not in visited:
                    s.append(y)
                    visited.add(y)
                    break
        return output
