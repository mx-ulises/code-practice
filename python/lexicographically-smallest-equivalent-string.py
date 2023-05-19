class Solution:
    def create_graph(s1: str, s2: str):
        graph = defaultdict(list)
        for i in range(len(s1)):
            a, b = s1[i], s2[i]
            graph[a].append(b)
            graph[b].append(a)
        return graph

    def group_chars(c: str, visited, graph):
        s = [c]
        group = []
        minimal = c
        while s:
            a = s.pop()
            if a in visited:
                continue
            visited.add(a)
            group.append(a)
            minimal = min(minimal, a)
            for b in graph[a]:
                s.append(b)
        return minimal, group

    def get_char_to_min(groups):
        char_to_min = {}
        for minimal, group in groups:
            for c in group:
                char_to_min[c] = minimal
        return char_to_min

    def get_smallest_equivalent(base_str, char_to_min):
        smallest_equivalent = []
        for a in base_str:
            smallest_equivalent.append(char_to_min.get(a, a))
        return "".join(smallest_equivalent)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = Solution.create_graph(s1, s2)
        visited = set()
        groups = []
        for c in graph:
            if c not in visited:
                minimal, group = Solution.group_chars(c, visited, graph)
                groups.append((minimal, group))
        print(groups)
        char_to_min = Solution.get_char_to_min(groups)
        smallest_equivalent = Solution.get_smallest_equivalent(baseStr, char_to_min)
        return smallest_equivalent
