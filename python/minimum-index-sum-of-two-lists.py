class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings_least_sum = []
        least_index_sum = len(list1) + len(list2)
        strings = {list1[i]: i for i in range(len(list1))}
        for i in range(len(list2)):
            s = list2[i]
            if s in strings and strings[s] + i < least_index_sum:
                least_index_sum = strings[s] + i
                common_strings_least_sum = [s]
            elif s in strings and strings[s] + i == least_index_sum:
                common_strings_least_sum.append(s)
        return common_strings_least_sum
