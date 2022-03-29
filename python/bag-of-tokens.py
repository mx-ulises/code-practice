class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        score = 0
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        while i != j:
            if tokens[i] <= power:
                power -= tokens[i]
                i += 1
                score += 1
            elif score:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
        if tokens[i] <= power:
            power -= tokens[i]
            i += 1
            score += 1
        return score
