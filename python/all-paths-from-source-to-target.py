class Solution:
    def get_paths(graph: List[List[int]], current_path: List[int], solutions: List[List[int]], target: int):
        tail = current_path[-1]
        if tail == target:
            solutions.append(list(current_path))
        else:
            for new_tail in graph[tail]:
                current_path.append(new_tail)
                Solution.get_paths(graph, current_path, solutions, target)
                current_path.pop()


    def solution_1(graph: List[List[int]]) -> List[List[int]]:
        solutions = []
        current_path = [0]
        target = len(graph) - 1
        Solution.get_paths(graph, current_path, solutions, target)
        return solutions


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        solutions = []
        current_path = [0]
        target = len(graph) - 1
        Solution.get_paths(graph, current_path, solutions, target)
        return solutions
