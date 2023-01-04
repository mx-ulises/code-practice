CHAR_MAP = "0123456789abcdef"

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 4294967295 + (num + 1)
        hex_num = []
        while num:
            h = num % 16
            hex_num.append(CHAR_MAP[h])
            num = num // 16
        hex_num.reverse()
        return "".join(hex_num)
