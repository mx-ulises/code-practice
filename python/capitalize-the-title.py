class Solution:
    def lower_case(c: str) -> str:
        if 'A' <= c and c <= 'Z':
            return chr(ord(c) - ord('A') + ord('a'))
        return c


    def upper_case(c: str) -> str:
        if 'a' <= c and c <= 'z':
            return chr(ord(c) - ord('a') + ord('A'))
        return c


    def capitalize_word(word: str) -> str:
        word_array = []
        for c in word:
            word_array.append(Solution.lower_case(c))
        if 2 < len(word_array):
            word_array[0] = Solution.upper_case(word_array[0])
        return "".join(word_array)


    def capitalizeTitle(self, title: str) -> str:
        title_capitalized = map(Solution.capitalize_word, title.split())
        return " ".join(title_capitalized)
