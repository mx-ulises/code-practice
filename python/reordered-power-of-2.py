class Solution:
    def get_power_key(power: int):
        power_key = []
        while 0 < power:
            power_key.append(str(power % 10))
            power //= 10
        power_key.sort()
        power_key.reverse()
        return "".join(power_key)

    def get_power_keys(limit: int) -> List:
        i = 1
        power_keys = set([])
        while i <= limit:
            power_keys.add(Solution.get_power_key(i))
            i <<= 1
        return power_keys

    def reorderedPowerOf2(self, n: int) -> bool:
        power_key = Solution.get_power_key(n)
        power_keys = Solution.get_power_keys(int(power_key))
        return power_key in power_keys
