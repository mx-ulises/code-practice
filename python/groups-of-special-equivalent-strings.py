class Solution:
    def get_word_key(word: str) -> str:
        char_swap_group = [[], []]
        for i in range(len(word)):
            char_swap_group[i & 1].append(word[i])
        char_swap_group[0].sort()
        char_swap_group[1].sort()
        return "".join(char_swap_group[0] + char_swap_group[1])

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:
            key = Solution.get_word_key(word)
            groups.add(key)
        return len(groups)
