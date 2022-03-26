class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        num3 = []
        carry = 0
        num_max, num_min = num1, num2
        if len(num1) < len (num2):
            num_min, num_max = num1, num2
        for i in range(len(num_min)):
            j = -1 - i
            n = int(num_min[j]) + int(num_max[j]) + carry
            carry, d = n // 10, n % 10
            num3.append(str(d))
        for i in range(len(num_min), len(num_max)):
            j = -1 - i
            n = int(num_max[j]) + carry
            carry, d = n // 10, n % 10
            num3.append(str(d))
        if carry:
            num3.append(str(carry))
        num3.reverse()
        return "".join(num3)
