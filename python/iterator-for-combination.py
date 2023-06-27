class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.k = combinationLength
        self.indexes = [(i, len(self.characters) - self.k + i) for i in range(self.k)]

    def next(self) -> str:
        next_word_list = [self.characters[pair[0]] for pair in self.indexes]
        while self.indexes and self.indexes[-1][0] == self.indexes[-1][1]:
            self.indexes.pop()
        if self.indexes:
            i, limit = self.indexes.pop()
            while len(self.indexes) < self.k:
                self.indexes.append((i + 1, limit))
                i += 1
                limit += 1
        return "".join(next_word_list)

    def hasNext(self) -> bool:
        return len(self.indexes) == self.k
