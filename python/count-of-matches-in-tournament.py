class Solution:
    def algorithm(n: int) -> int:
        match_count = 0
        while 1 < n:
            is_odd = n & 1
            match_in_round = n // 2
            match_count += match_in_round
            n = match_in_round + is_odd
        return match_count

    def numberOfMatches(self, n: int) -> int:
        # return algorithm(n)
        return n - 1
