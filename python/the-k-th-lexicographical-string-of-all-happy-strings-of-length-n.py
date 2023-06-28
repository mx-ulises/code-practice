ALPHABETH = ["a", "b", "c"]

class Solution:
    def get_happy_string(n: int, k: int, i: int, s: List[str]) -> (int, str):
        if len(s) == n:
            i += 1
            return (i, "".join(s))
        for c in ALPHABETH:
            if len(s) == 0 or s[-1] != c:
                s.append(c)
                i, happy_string = Solution.get_happy_string(n, k, i, s)
                if i == k:
                    return (i, happy_string)
                s.pop()
        return (i, "")

    def getHappyString(self, n: int, k: int) -> str:
        _, happy_string = Solution.get_happy_string(n, k, 0, [])
        return happy_string
