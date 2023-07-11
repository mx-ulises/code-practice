class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        score = 0
        maximal = 0
        answer = []
        for num in nums:
            maximal = max(maximal, num)
            conversion_value = num + maximal
            score += conversion_value
            answer.append(score)
        return answer
