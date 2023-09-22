class Solution:
    def is_palindrome(s: str, mem: List[str]) -> bool:
        if s in mem:
            return mem[s]
        n = len(s)
        mem[s] = True
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                mem[s] = False
                break
        return mem[s]

    def partition(self, s: str) -> List[List[str]]:
        palindrome_partitions = [([s[0]], True)]
        mem = {c: True for c in s}
        for i in range(1, len(s)):
            c = s[i]
            new_palindrome_partitions = []
            while palindrome_partitions:
                partition, is_valid = palindrome_partitions.pop()
                if is_valid:
                    new_palindrome_partitions.append((partition + [c], True))
                new_partitioning = partition[:len(partition) - 1] + [partition[-1] + c]
                is_valid = Solution.is_palindrome(new_partitioning[-1], mem)
                new_palindrome_partitions.append((new_partitioning, is_valid))
            palindrome_partitions = new_palindrome_partitions
        return [partition for (partition, is_valid) in palindrome_partitions if is_valid]
