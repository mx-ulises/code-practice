class Solution:
    def load_chars(row_map: Dict[str, int], row: str, row_num: int):
        for c in row:
            row_map[c] = row_num

    def is_valid_word(word: str, row_map: Dict[str, int]) -> bool:
        expected_line = row_map[word[0].lower()]
        valid_word = True
        for c in word:
            if row_map[c.lower()] != expected_line:
                valid_word = False
                break
        return valid_word

    def findWords(self, words: List[str]) -> List[str]:
        row_map = {}
        Solution.load_chars(row_map, "qwertyuiop", 1)
        Solution.load_chars(row_map, "asdfghjkl", 2)
        Solution.load_chars(row_map, "zxcvbnm", 3)
        output = []
        for word in words:
            if Solution.is_valid_word(word, row_map):
                output.append(word)
        return output
