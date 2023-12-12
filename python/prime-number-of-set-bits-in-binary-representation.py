PRIMES = set([2, 3, 5, 7, 11, 13, 17, 19])

class Solution:
    def get_bits(num: int, bits: Dict[int, int]) -> bool:
        if num not in bits:
            bits[num] = Solution.get_bits(num >> 1, bits) + (num & 1)
        return bits[num]

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        bits = {0: 0}
        while left <= right:
            if Solution.get_bits(left, bits) in PRIMES:
                count += 1
            left += 1
        return count
