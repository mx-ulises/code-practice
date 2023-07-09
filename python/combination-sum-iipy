class Solution:
    def get_candidate_count(candidates: List[int], target: int):
        candidate_count_dict = defaultdict(lambda: 0)
        for candidate in candidates:
            if candidate <= target:
                candidate_count_dict[candidate] += 1
        return [(candidate, candidate_count_dict[candidate]) for candidate in candidate_count_dict]

    def get_combination_list(candidate_count, target, prefix, current_sum, output):
        if current_sum == target:
            output.append(list(prefix))
        if current_sum < target and 0 < len(candidate_count):
            candidate, count = candidate_count.pop()
            added = 0
            Solution.get_combination_list(candidate_count, target, prefix, current_sum, output)
            while added < count and current_sum <= target:
                added += 1
                prefix.append(candidate)
                current_sum += candidate
                Solution.get_combination_list(candidate_count, target, prefix, current_sum, output)
            while 0 < added:
                prefix.pop()
                current_sum -= candidate
                added -= 1
            candidate_count.append((candidate, count))

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidate_count = Solution.get_candidate_count(candidates, target)
        prefix = []
        current_sum = 0
        output = []
        Solution.get_combination_list(candidate_count, target, prefix, current_sum, output)
        return output
