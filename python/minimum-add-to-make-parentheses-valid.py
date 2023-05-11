class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additional_chars = 0
        for c in s:
            if c == "(":
                balance += 1
            if c == ")":
                balance -= 1
            if balance < 0:
                additional_chars += 1
                balance = 0
        additional_chars += balance
        return additional_chars
