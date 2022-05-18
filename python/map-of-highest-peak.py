NEIGHBOORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid(i, j, m, n, isWater):
    if 0 <= i < m and 0 <= j < n and isWater[i][j] == -1:
        return True
    return False

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    dq.append((i, j, 0))
                isWater[i][j] = -1
        while dq:
            i, j, h = dq.popleft()
            if is_valid(i, j, m, n, isWater):
                isWater[i][j] = h
                for offset_x, offset_y in NEIGHBOORS:
                    i_next = i + offset_x
                    j_next = j + offset_y
                    dq.append((i_next, j_next, h + 1))
        return isWater
