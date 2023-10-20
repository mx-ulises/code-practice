class Solution:
    def sortString(self, s: str) -> str:
        output = []
        char_count = defaultdict(lambda: 0)
        for c in s:
            char_count[c] += 1
        chars = list(char_count.keys())
        chars.sort()
        direction = 1
        while len(output) < len(s):
            for i in range(0, len(chars)):
                c = chars[i]
                if direction == -1:
                    c = chars[len(chars) - i - 1]
                if char_count[c]:
                    char_count[c] -= 1
                    output.append(c)
            direction *= -1
        return "".join(output)
