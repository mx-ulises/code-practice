class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_ranges = {}
        char_order = []
        for i in range(len(s)):
            c = s[i]
            if c not in char_ranges:
                char_ranges[c] = [i, i]
                char_order.append(c)
            char_ranges[c][1] = i
        output = [char_ranges[char_order[0]][1]]
        for c in char_order:
            start, end = char_ranges[c]
            if output[-1] < start:
                output.append(end)
            output[-1] = max(output[-1], end)
        current_sum = 0
        for i in range(len(output)):
            output[i] -= (current_sum - 1)
            current_sum += output[i]
        return output
