class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = (m + n) * mean
        missing = total - sum(rolls)
        output = []
        while n:
            candidate = max(1, min(missing - n + 1, 6))
            n -= 1
            missing -= candidate
            output.append(candidate)
        if missing != 0:
            return []
        return output
