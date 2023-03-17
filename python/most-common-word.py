SEPARATORS = set(list("!?',;."))
class Solution:
    def normalize(paragraph: str) -> str:
        new_paragraph = []
        for c in paragraph:
            if c in SEPARATORS:
                new_paragraph.append(" ")
            else:
                new_paragraph.append(c.lower())
        return "".join(new_paragraph)


    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = Solution.normalize(paragraph)
        word_count = defaultdict(lambda: 0)
        for word in paragraph.split():
            word_count[word] += 1
        for word in banned:
            word_count[word] = 0
        max_frequency, most_common_word = 0, ""
        for word in word_count:
            if max_frequency < word_count[word]:
                max_frequency = word_count[word]
                most_common_word = word
        return most_common_word
