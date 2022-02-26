class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            p2w = {}
            w2p = {}
            valid = True
            if len(word) != len(pattern):
                continue
            for i in range(len(word)):
                w = word[i]
                p = pattern[i]
                if p not in p2w and w not in w2p:
                    p2w[p] = w
                    w2p[w] = p
                elif p2w.get(p, None) != w or w2p.get(w, None) != p:
                    valid = False
                    break
            if valid:
                output.append(word)
        return output
