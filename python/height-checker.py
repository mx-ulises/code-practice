class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = list(heights)
        heights_sorted.sort()
        not_in_order = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                not_in_order += 1
        return not_in_order
