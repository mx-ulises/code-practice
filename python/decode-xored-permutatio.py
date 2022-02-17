class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        n_sum_xor = 0
        for i in range(1, n + 1):
            n_sum_xor ^= i
        encoded_current_term = 0
        encoded_sum_term = 0
        for i in encoded:
            encoded_current_term ^= i
            encoded_sum_term ^= encoded_current_term
        perm = [n_sum_xor ^ encoded_sum_term]
        for i in encoded:
            perm.append(perm[-1] ^ i)
        return perm
