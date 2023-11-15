class Solution:
    def get_best(tree: Dict[int,List[int]], values: List[int], visited: Set[int], node: int) -> Tuple[int]:
        visited.add(node)
        best = 0
        total = 0
        leaf = True
        for child in tree[node]:
            if child in visited:
                continue
            leaf = False
            child_best, child_total = Solution.get_best(tree, values, visited, child)
            total += child_total
            best += child_best
        if leaf:
            return 0, values[node]
        node_best = max(values[node] + best, total)
        return node_best, total + values[node]

    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        tree = defaultdict(list)
        visited = set()
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        return Solution.get_best(tree, values, visited, 0)[0]
