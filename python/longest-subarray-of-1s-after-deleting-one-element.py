class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_segment_size = 0
        current_segment_size = 0
        longest_size = 0
        is_there_zeros = False
        for num in nums:
            if num == 1:
                current_segment_size += 1
            else:
                candidate_size = prev_segment_size + current_segment_size
                longest_size = max(longest_size, candidate_size)
                prev_segment_size = current_segment_size
                current_segment_size = 0
                is_there_zeros = True
        candidate_size = prev_segment_size + current_segment_size
        longest_size = max(longest_size, candidate_size)
        if is_there_zeros == False:
            longest_size -= 1
        return longest_size
