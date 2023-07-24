class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        output = []
        maximal = 0
        current = 0
        for c in seq:
            if c == "(":
                output.append(current)
                current += 1
                maximal = max(maximal, current)
            else:
                current -= 1
                output.append(current)
        mean = maximal // 2
        for i in range(len(output)):
            output[i] = output[i] < mean
        return output
