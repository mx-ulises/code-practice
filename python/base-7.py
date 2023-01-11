class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        base_7 = deque()
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num
        while num:
            base_7.appendleft(str(num % 7))
            num = num // 7
        if is_negative:
            base_7.appendleft("-")
        return "".join(base_7)
