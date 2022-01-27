def isNewProvince(isConnected, i, visited, n):
    if visited[i]:
        return False
    visited[i] = True
    for j in range(n):
        if isConnected[i][j]:
            isNewProvince(isConnected, j, visited, n)
    return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        provinces_count = 0
        for i in range(n):
            if isNewProvince(isConnected, i, visited, n):
                provinces_count += 1
        return provinces_count
