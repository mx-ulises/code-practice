class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_penalty = 0
        for comming in customers:
            if comming == "Y":
                current_penalty += 1
        minimal_penalty = current_penalty
        minimal_hour = 0
        current_hour = 0
        for comming in customers:
            current_hour += 1
            if comming == "N":
                current_penalty += 1
            else:
                current_penalty -= 1
            if current_penalty < minimal_penalty:
                minimal_penalty = current_penalty
                minimal_hour = current_hour
        return minimal_hour
