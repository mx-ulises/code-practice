VOWELS = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
VOWEL_PLACEHOLDER = '-'

class Solution:
    def remove_vowels(s: str) -> (List[str], List[str]):
        s_array = list(s)
        vowels = []
        for i in range(len(s_array)):
            if s_array[i] in VOWELS:
                vowels.append(s_array[i])
                s_array[i] = VOWEL_PLACEHOLDER
        return vowels, s_array

    def add_vowels(s_array: List[str], vowels: List[str]) -> List[str]:
        j = 0
        for i in range(len(s_array)):
            if s_array[i] == VOWEL_PLACEHOLDER:
                s_array[i] = vowels[j]
                j += 1

    def sortVowels(self, s: str) -> str:
        vowels, s_array = Solution.remove_vowels(s)
        vowels.sort()
        Solution.add_vowels(s_array, vowels)
        return "".join(s_array)
