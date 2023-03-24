class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        minimal = 0
        maximal = n
        output = []
        for c in s:
            if c == "I":
                output.append(minimal)
                minimal += 1
            if c == "D":
                output.append(maximal)
                maximal -= 1
        output.append(minimal)
        return output
