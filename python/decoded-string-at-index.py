class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        current_word = []
        word_graph = []
        current_tape_size = 0
        for c in s:
            if 'a' <= c <= 'z':
                current_word.append(c)
            if '2' <= c <= '9':
                d = int(c)
                if current_word:
                    start = current_tape_size
                    end = current_tape_size + len(current_word)
                    current_tape_size += len(current_word)
                    word_graph.append({
                        "word": "".join(current_word),
                        "start": start,
                        "end": end,
                        "repeat": d,
                    })
                    current_tape_size *= d
                elif word_graph:
                    word_graph[-1]["repeat"] *= d
                    current_tape_size *= d
                current_word = []
        if current_word:
            start = current_tape_size
            end = current_tape_size + len(current_word)
            current_tape_size += len(current_word)
            word_graph.append({
                "word": "".join(current_word),
                "start": start,
                "end": end,
                "repeat": 1,
            })
        k = k - 1
        while k:
            word = word_graph.pop()
            k = k % word["end"]
            if word["start"] <= k:
                i = k - word["start"]
                return word["word"][i]
        return word_graph[0]["word"][0]
