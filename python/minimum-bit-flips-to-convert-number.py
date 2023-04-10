class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = start ^ goal
        flip_count = 0
        while flips:
            if flips & 1:
                flip_count += 1
            flips = flips >> 1
        return flip_count
