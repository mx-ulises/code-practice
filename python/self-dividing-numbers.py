class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = []
        for i in range(left, right + 1):
            s = str(i)
            include = True
            for d in map(int, list(s)):
                if d == 0 or i % d:
                    include = False
                    break
            if include:
                numbers.append(i)
        return numbers
