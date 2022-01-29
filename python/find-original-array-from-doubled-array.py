class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count_dict = defaultdict(lambda: 0)
        output = []
        for x in changed:
            count_dict[x] += 1
        numbers = list(count_dict.keys())
        numbers.sort()
        for x in numbers:
            y = x * 2
            while 0 < count_dict[x]:
                output.append(x)
                count_dict[x] -= 1
                count_dict[y] -= 1
                if count_dict[y] < 0:
                    return []
        return output
