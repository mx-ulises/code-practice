CHAR_MAP = {"0": 0, "1": 1}

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        out = []
        i_a, i_b = len(a), len(b)
        while i_a or i_b:
            d = c
            if i_a:
                i_a -= 1
                d += CHAR_MAP[a[i_a]]
            if i_b:
                i_b -= 1
                d += CHAR_MAP[b[i_b]]
            out.append(d % 2)
            c = d // 2
        if c:
            out.append(c)
        out_char = list(map(str, out))
        out_char.reverse()
        return "".join(out_char)
