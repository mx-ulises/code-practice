class Solution:
    def minFlips(self, target: str) -> int:
        current = "0"
        count = 0
        for b in target:
            if current != b:
                current = b
                count += 1
        return count
