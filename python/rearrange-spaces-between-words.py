class Solution:
    def get_space_count(text: str) -> int:
        space_count = 0
        for c in text:
            if c == " ":
                space_count += 1
        return space_count

    def reorderSpaces(self, text: str) -> str:
        space_count = Solution.get_space_count(text)
        words = [word for word in text.split() if len(word)]
        gaps = len(words) - 1
        if 0 < gaps:
            spaces = " " * (space_count // gaps)
            end = " " * (space_count % gaps)
            return spaces.join(words) + end
        return words[0] + (" " * space_count)
