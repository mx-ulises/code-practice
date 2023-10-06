class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [0] * len(s)
        for i in range(len(s)):
            output[indices[i]] = s[i]
        return "".join(output)
