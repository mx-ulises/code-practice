class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        i = 1
        j = 0
        m = len(target)
        while i <= n and j < m:
            operations.append("Push")
            if i == target[j]:
                j += 1
            else:
                operations.append("Pop")
            i += 1
        return operations
