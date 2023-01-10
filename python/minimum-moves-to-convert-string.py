class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        move_count = 0
        while i < len(s):
            if s[i] == "X":
                i += 3
                move_count += 1
            else:
                i += 1
        return move_count
