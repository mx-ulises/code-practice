def solution_1(flips):
    left = []
    right = []
    prefix_aligned_count = 0
    for i in range(1, len(flips) + 1):
        heappush(right, flips[i - 1])
        while right and right[0] <= i:
            heappush(left, heappop(right))
        if not right:
            prefix_aligned_count += 1
    return prefix_aligned_count

def solution_2(flips):
    flip_sum = 0
    consecutive_sum = 0
    prefix_aligned_count = 0
    for i in range(len(flips)):
        flip_sum += flips[i]
        consecutive_sum += (i + 1)
        if flip_sum == consecutive_sum:
            prefix_aligned_count += 1
    return prefix_aligned_count

def solution_3(flips):
    max_flip = 0
    prefix_aligned_count = 0
    for i in range(len(flips)):
        max_flip = max(max_flip, flips[i])
        if (i + 1) == max_flip:
            prefix_aligned_count += 1
    return prefix_aligned_count

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        return solution_3(flips)
