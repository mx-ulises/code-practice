class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = []
        ch_seen = False
        for c in word:
            output.append(c)
            if not ch_seen and c == ch:
                output.reverse()
                ch_seen = True
        return "".join(output)
