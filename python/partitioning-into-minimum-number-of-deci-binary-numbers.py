class Solution:
    def minPartitions(self, n: str) -> int:
        partitions = ord(max(n)) - 48 # ord('0') == 48
        return partitions
