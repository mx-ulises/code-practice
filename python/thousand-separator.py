class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        output = []
        point = 0
        while n:
            output.append(str(n % 10))
            n = n // 10
            point += 1
            if point % 3 == 0:
                output.append(".")
        if output[-1] == ".":
            output.pop()
        output.reverse()
        return "".join(output)
