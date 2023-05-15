class Solution:
    def countVowelStrings(self, n: int) -> int:
        char_options = 5
        strings_ending_in_char = [1] * char_options
        cummulative_sum = 0
        for i in range(n):
            cummulative_sum = 0
            for j in range(char_options):
                cummulative_sum += strings_ending_in_char[j]
                strings_ending_in_char[j] = cummulative_sum
        return cummulative_sum
