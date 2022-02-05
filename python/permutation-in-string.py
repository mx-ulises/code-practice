def is_empty(counter):
    for c in counter:
        if counter[c]:
            return False
    return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counter = defaultdict(lambda: 0)
        n = len(s1)
        for c in s1:
            counter[c] += 1
        for i in range(n):
            counter[s2[i]] -= 1
        if is_empty(counter):
            return True
        for i in range(n, len(s2)):
            counter[s2[i- n]] += 1
            counter[s2[i]] -= 1
            if is_empty(counter):
                return True
        return False
