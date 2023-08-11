class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        current_sum = 0
        max_satisfaction = 0
        current_satisfaction = 0
        while satisfaction:
            current_sum += satisfaction.pop()
            current_satisfaction += current_sum
            max_satisfaction = max(max_satisfaction, current_satisfaction)
        return max_satisfaction
