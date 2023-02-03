MOD = 1337

class Solution:
    def pow(base, exp):
        result = 1
        while exp:
            if exp & 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            exp >>= 1
        return result

    def super_pow(base: int, b: List[int]) -> int:
        if len(b) == 0:
            return 1
        c = b.pop()
        return (Solution.pow(Solution.super_pow(base, b), 10) * Solution.pow(base, c)) % MOD

    def superPow(self, a: int, b: List[int]) -> int:
        return Solution.super_pow(a % MOD, b)
