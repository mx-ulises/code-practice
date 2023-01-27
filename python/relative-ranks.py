class Solution:
    def get_rank(a: int) -> str:
        if a == 1:
            return "Gold Medal"
        if a == 2:
            return "Silver Medal"
        if a == 3:
            return "Bronze Medal"
        return str(a)


    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [(score[i], i) for i in range(len(score))]
        ranks.sort()
        answer = [""] * len(score)
        a = 1
        while ranks:
            _, i = ranks.pop()
            answer[i] = Solution.get_rank(a)
            a += 1
        return answer
