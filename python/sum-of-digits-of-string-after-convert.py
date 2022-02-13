class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabeth = "abcdefghijklmnopqrstuvwxyz"
        alphabeth_map = {}
        for c in alphabeth:
            alphabeth_map[c] = str(ord(c) - ord('a') + 1)
        # Convert
        num_array = []
        for c in s:
            num_array.append(alphabeth_map[c])
        num = "".join(num_array)
        #transform
        for _ in range(k):
            num_int = 0
            for d in num:
                num_int += int(d)
            num = str(num_int)
        return num
