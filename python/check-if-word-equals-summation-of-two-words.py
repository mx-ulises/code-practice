class Solution:
    def get_numeric_value(word: str) -> int:
        number = 0
        for c in word:
            number = number * 10 + ord(c) - ord('a')
        return number

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_number = Solution.get_numeric_value(firstWord)
        second_number = Solution.get_numeric_value(secondWord)
        target_number = Solution.get_numeric_value(targetWord)
        return (first_number + second_number) == target_number
