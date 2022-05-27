class Solution:
    def lengthLongestPath(self, dir_tree: str) -> int:
        s = []
        largest_path = 0
        for entry in dir_tree.split('\n'):
            entry_split = entry.split('\t')
            while len(entry_split) <= len(s):
                s.pop()
            s.append(entry_split[-1])
            if '.' in entry_split[-1]:
                current_size = sum(map(len, s)) + len(s) - 1
                largest_path = max(largest_path, current_size)
        return largest_path
