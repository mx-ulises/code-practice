class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        h = []
        while score:
            row = score.pop()
            heappush(h, (-row[k], row))
        while h:
            score.append(heappop(h)[1])
        return score
