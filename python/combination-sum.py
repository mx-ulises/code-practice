class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates.reverse()
        combinations = []
        prefixes = [(0, [])]
        for candidate in candidates:
            new_prefixes = []
            for (prefix_sum, prefix) in prefixes:
                current_sum = prefix_sum
                while current_sum < target:
                    new_prefixes.append((current_sum, list(prefix)))
                    current_sum += candidate
                    prefix.append(candidate)
                if current_sum == target:
                    combinations.append(prefix)
            prefixes = new_prefixes
        return combinations
