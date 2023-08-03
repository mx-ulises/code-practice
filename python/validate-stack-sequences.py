class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i, j = 0, 0
        while i < len(pushed):
            s.append(pushed[i])
            while s and s[-1] == popped[j]:
                s.pop()
                j += 1
            i += 1
        return len(s) == 0
