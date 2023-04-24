class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = defaultdict(list)
        groups = []
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            group_map[size].append(i)
            if len(group_map[size]) == size:
                groups.append(group_map[size])
                group_map[size] = []
        return groups
