class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimal, count = k, 0
        for i in range(len(blocks)):
            if k <= i:
                minimal = min(minimal, count)
            if blocks[i] == "W":
                count += 1
            if k <= i and blocks[i - k] == "W":
                count -= 1
        return min(minimal, count)
