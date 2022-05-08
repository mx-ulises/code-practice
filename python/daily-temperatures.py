class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        s = [(temperatures[0], 0)]
        answer = [0] * n
        for i in range(1, n):
            while s and s[-1][0] < temperatures[i]:
                answer[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append((temperatures[i], i))
        return answer
