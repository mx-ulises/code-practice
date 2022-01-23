class Trie:

    def __init__(self):
        self.succesors = {}

    def insert(self, word: str) -> None:
        current = self.succesors
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c];
        current["*"] = {}

    def search(self, word: str) -> bool:
        current = self.succesors
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return "*" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.succesors
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True
