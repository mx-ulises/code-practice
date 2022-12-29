class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)
        output = []
        while 0 < i:
            i -= 1
            if s[i] == "#":
                offset = int(s[i - 2] + s[i - 1]) - 1
                i -= 2
            else:
                offset = int(s[i]) - 1
            output.append(chr(ord('a') + offset))
        output.reverse()
        return "".join(output)
