class Solution:
    def get_word_len(word: List[str]) -> int:
        return sum([len(segment) for segment in word])

    def get_word_index_and_offset(word: List[str], segment_index: int, segment_pos: int, offset: int) -> (int, int):
        if (segment_pos + 1) == len(word[segment_index]):
            offset += len(word[segment_index])
            segment_index += 1
        return segment_index, offset


    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if Solution.get_word_len(word1) != Solution.get_word_len(word2):
            return False
        index = 0
        offset_1, offset_2 = 0, 0
        segment_index_1, segment_index_2 = 0, 0
        while segment_index_1 < len(word1):
            i = index - offset_1
            j = index - offset_2
            if word1[segment_index_1][i] != word2[segment_index_2][j]:
                return False
            segment_index_1, offset_1 = Solution.get_word_index_and_offset(word1, segment_index_1, i, offset_1)
            segment_index_2, offset_2 = Solution.get_word_index_and_offset(word2, segment_index_2, j, offset_2)
            index += 1
        return True
