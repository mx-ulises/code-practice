class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        current_int = []
        integers = set([])
        for c in word:
            if "0" <= c <= "9":
                current_int.append(c)
            else:
                if current_int:
                    integers.add(int("".join(current_int)))
                    current_int = []
        if current_int:
            integers.add(int("".join(current_int)))
        return len(integers)
