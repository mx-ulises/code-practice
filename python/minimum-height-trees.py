class Solution:
    def build_graph(edges: List[List[int]]) -> Dict[int, Set[int]]:
        graph = defaultdict(set)
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)
        return graph


    def get_node_ranking(graph: Dict[int, Set[int]]) -> Dict[int, Set[int]]:
        node_ranking = defaultdict(set)
        for node in graph:
            rank = len(graph[node])
            node_ranking[rank].add(node)
        return node_ranking


    def update_parent(node: int, node_ranking: Dict[int, Set[int]], graph: Dict[int, Set[int]]):
        parent = list(graph[node])[0]
        node_ranking[len(graph[parent])].remove(parent)
        graph[parent].remove(node)
        node_ranking[len(graph[parent])].add(parent)


    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = Solution.build_graph(edges)
        node_ranking = Solution.get_node_ranking(graph)
        remaining_nodes = set([i for i in range(n)])
        while 2 < len(remaining_nodes):
            leaves = node_ranking[1]
            node_ranking[1] = set()
            for leaf in leaves:
                # Update leaf's parent ranking
                Solution.update_parent(leaf, node_ranking, graph)
                # Remove leaf from memory
                del graph[leaf]
                remaining_nodes.remove(leaf)
        return list(remaining_nodes)
