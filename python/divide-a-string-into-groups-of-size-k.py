class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        current_word = []
        for i in range(len(s)):
            current_word.append(s[i])
            if len(current_word) == k:
                output.append("".join(current_word))
                current_word = []
        if current_word:
            while len(current_word) < k:
                current_word.append(fill)
            output.append("".join(current_word))
        return output
