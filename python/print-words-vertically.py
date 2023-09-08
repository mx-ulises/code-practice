class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        vertical = []
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                if j == len(vertical):
                    vertical.append([])
                while len(vertical[j]) < i:
                    vertical[j].append(" ")
                vertical[j].append(word[j])
        vertical_words = ["".join(row) for row in vertical]
        return vertical_words
