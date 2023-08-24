class Solution:
    def get_power_key(power: int) -> int:
        power_key = []
        while 0 < power:
            power_key.append(str(power % 10))
            power //= 10
        power_key.sort()
        power_key.reverse()
        return int("".join(power_key))

    def check_power_key(power_key: int) -> bool:
        i = 1
        while i <= power_key:
            if Solution.get_power_key(i) == power_key:
                return True
            i <<= 1
        return False

    def reorderedPowerOf2(self, n: int) -> bool:
        power_key = Solution.get_power_key(n)
        return Solution.check_power_key(power_key)
