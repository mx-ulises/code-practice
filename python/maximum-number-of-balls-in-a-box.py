def get_key(x):
    key = 0
    while x:
        key += x % 10
        x = x // 10
    return key

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        key_count = defaultdict(lambda: 0)
        maximal = 0
        for x in range(lowLimit, highLimit + 1):
            key = get_key(x)
            key_count[key] += 1
            maximal = max(maximal, key_count[key])
        return maximal
